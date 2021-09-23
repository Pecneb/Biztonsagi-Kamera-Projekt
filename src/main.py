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
    parser.add_argument('vsrc', metavar='[video source path]', help='path to the video source (0 to use webcam).')
    # mode: kamera or background subtraction
    parser.add_argument('--mode', help='Choose: show camera/video (play) or background subtraction (md) mode.', default='cam')
    # choose algo for background subtraction
    parser.add_argument('--algo', help='Choose what background subtractor algo to use: MOG2 or KNN', default='MOG2')
    # parse args
    args = parser.parse_args()
    
    if args.mode == 'play':
        if args.vsrc == '0':
            kamera((int)(args.vsrc))
        else:
            kamera(args.vsrc)
    elif args.mode == 'md':
        if args.vsrc == '0':
            bgsub((int)(args.vsrc), args.algo)
        else:
            bgsub(args.vsrc, args.algo)

if __name__=="__main__":
    main()
