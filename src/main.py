# import sys
# import os
import argparse
import cv2 as cv
import numpy
import matplotlib.pyplot as plt
from kamera import kamera

def main():
    parser = argparse.ArgumentParser(description='Security Camera with motion detection:')
    parser.add_argument('vsrc', metavar='[video source path]', help='path to the video source')
    args = parser.parse_args()
    
    if args.vsrc in '0123456789':
        kamera(int(args.vsrc))

    kamera(args.vsrc)

if __name__=="__main__":
    main()
