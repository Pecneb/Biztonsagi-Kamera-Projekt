import cv2

import numpy

from matplotlib import pyplot

import sys

import argparse

def record(vSource, outputName):
    '''
    This module is for recording videos via webcam.

    vSource is the webcam input source
    
    if using linux then it should be /dev/video[0..n]
    
    Press c to start recording
    
    Press q to stop and quit
    '''

    cap = cv2.VideoCapture(vSource)

    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    
    out = cv2.VideoWriter(outputName, fourcc, 20.00, (width, height))

    if not cap.isOpened():

        print("Cant open video!\n")
    
    capture = False

    while True:
        ret, frame = cap.read()
        
        if not ret:
            
            print("End of video!\n")
            
            break

        if cv2.waitKey(10) == ord('c'):

                print("Start recording!\n")

                capture = True

        cv2.imshow("Capture", frame)

        if capture:
        
            print("REC\n")

            out.write(frame)

        if cv2.waitKey(20) == ord('q'):
            
            break
    
    cap.release()

    out.release()

    print("Stop recording!")
    
    cv2.destroyAllWindows()

def main():

    parser = argparse.ArgumentParser(description='Playing and Recording videos. Press C to start recording Press Q to stop and quit.')

    parser.add_argument('--input', help='Path to the video or webcam. (For webcam use /dev/video[0..N]', default='video0')

    parser.add_argument('--output', help='Recorded video name/path', default='output.avi')

    args = parser.parse_args()

    vSource = args.input

    outputName = args.output

    record(vSource, outputName)

if __name__ == "__main__":
    
    main()