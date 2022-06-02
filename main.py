# import sys
# import os
import argparse
from bgsub import bgsub
import os
from datetime import date

def setup_dir():
    '''
    This function sets up the directory for recording videos of detections.
    First create detections dir if not already created.
    Then Created a directory for the current day.
    So each day gets a directory. And each video that has been recorded is saved under the current day,
    that has been recorded on.
    '''
    try:
        os.mkdir("detections")
        print("Creating directory: detections.")        
    except FileExistsError:
        print("Directory is already there!")

    try:
        os.mkdir(os.path.join("detections", date.strftime(date.today(),"%Y-%m-%d")))
        print("Creating todays directory.")
    except FileExistsError:
        print("Directory is already there!")

def main():
    # Using argparser to get command line arguments
    parser = argparse.ArgumentParser(description="Security Camera with motion detection.(quit with 'q', press 'q' to pause and resume)")
    # vsrc is an argument, the user should give in the command line, no matter what!
    parser.add_argument('--input', help='path to the video source (webcam is default).', default=0)
    # choose algo for background subtraction
    parser.add_argument('--algo', help='Choose the background subtraction algorythm MOG2 or KNN', default='MOG2', choices=['KNN', 'MOG2'])
    # use darknet or not
    parser.add_argument('--darknet', help='turn on darknet YOLO object detection and recognition', default=0, choices=['0','1'])
    # check if user wants video recording
    parser.add_argument('--record', help="Save detection into video or not. default is 0", default=0, choices=[0, 1], type=int)
    
    # parse args
    args = parser.parse_args()
    
    # check if input source is webcam or path to video
    try:
        input = int(args.input)
    except ValueError:
        input = args.input

    rec_flag = int(args.record)
    if(rec_flag):
        setup_dir()

    # call program loop 
    bgsub(input, args.algo, int(args.darknet), rec_flag)

if __name__=="__main__":
    main()
