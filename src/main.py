# import sys
# import os
import argparse
import cv2 as cv
import numpy
import matplotlib.pyplot as plt
from kamera import kamera

def main():
    # Using argparser to get command line arguments
    parser = argparse.ArgumentParser(description='Security Camera with motion detection:')
    # vsrc is an argument, the user should give in the command line, no matter what!
    parser.add_argument('vsrc', metavar='[video source path]', help='path to the video source')
    # parse args
    args = parser.parse_args()
    
    # if user gives video src 0-9, then its propably a kamera
    if args.vsrc in '0123456789':
        kamera(int(args.vsrc))
    # if not, then its a video
    kamera(args.vsrc)

if __name__=="__main__":
    main()
