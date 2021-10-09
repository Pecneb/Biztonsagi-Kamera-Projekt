# import sys
# import os
import argparse
import cv2 as cv
import numpy
import matplotlib.pyplot as plt
from kamera import kamera
from bgsub import bgsub

def main():
    # Using argparser to get command line arguments
    parser = argparse.ArgumentParser(description="Security Camera with motion detection.(quit with 'q')")
    # vsrc is an argument, the user should give in the command line, no matter what!
    parser.add_argument('--input', help='path to the video source (webcam is default).', default=0)
    # mode: kamera or background subtraction
    parser.add_argument('--bsAlgo', help='Choose the background subtraction algorythm MOG2 or KNN', default='MOG2')
    # choose algo for background subtraction
    parser.add_argument('--sensAlgo', help='Choose what type of motion detection to use: tm or tm2. tm is for less populated areas, tm2 is more stable', default='tm2')
    # parse args
    args = parser.parse_args()
    
    if args.input == 0:
        
        if args.bsAlgo == 'KNN':
        
            if args.sensAlgo == 'tm':
                bgsub(0, 'KNN', 'tm')
            else:
                bgsub(0, 'KNN', 'tm2')
        else:
        
            if args.sensAlgo == 'tm':
                bgsub(0, 'MOG2', 'tm')
            else:
                bgsub(0, 'MOG2', 'tm2')
    
    elif args.input != 0:
        
        if args.bsAlgo == 'KNN':
    
            if args.sensAlgo == 'tm':
                bgsub(args.input, 'KNN', 'tm')
            else:
                bgsub(args.input, 'KNN', 'tm2')
        else:
    
            if args.sensAlgo == 'tm':
                bgsub(args.input, 'MOG2', 'tm')
            else:
                bgsub(args.input, 'MOG2', 'tm2')

if __name__=="__main__":
    main()
