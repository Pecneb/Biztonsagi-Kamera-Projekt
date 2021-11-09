# import sys
# import os
import argparse
from bgsub import bgsub

def main():
    # Using argparser to get command line arguments
    parser = argparse.ArgumentParser(description="Security Camera with motion detection.(quit with 'q')")
    # vsrc is an argument, the user should give in the command line, no matter what!
    parser.add_argument('--input', help='path to the video source (webcam is default).', default=0)
    # mode: kamera or background subtraction
    parser.add_argument('--algo', help='Choose the background subtraction algorythm MOG2 or KNN', default='MOG2', choices=['KNN', 'MOG2'])
    # choose algo for background subtraction
    # parser.add_argument('--sensAlgo', help='Choose what type of motion detection to use: camshift or contour. Contour detection can track multiple objects', default='tm2', choices=['camshift', 'contour'])
    # parse args
    args = parser.parse_args()
    
    # Use webcam as video source
    if args.input == 0:
        # Using KNN algorythm for background subtraction
        if args.algo == 'KNN':
            bgsub(0, 'KNN')
        # Using MOG2 algorythm for background subtraction
        elif args.algo == 'MOG2':
            bgsub(0, 'MOG2')
    # Specify video source
    elif args.input != 0:
        # Using KNN algorythm for background subtraction
        if args.algo == 'KNN':
            bgsub(args.input, 'KNN')
        # Using MOG2 algorythm for background subtraction
        elif args.algo == 'MOG2':
            bgsub(args.input, 'MOG2')

if __name__=="__main__":
    main()
