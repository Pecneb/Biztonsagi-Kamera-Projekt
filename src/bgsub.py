import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from oqqupation import is_oqqupied
from track_motion import track_motion
from find_anomaly import find_anomaly
from track_motion2 import track_motion2

GREEN = [0,255,0]
RED = [0,0,255]


'''
Background subtraction module
'''
def bgsub(vsrc, bgAlgo, sensAlgo):
    # choose what algorythm to use: MOG2 or KKN
    if bgAlgo == 'MOG2':
        backSub = cv.createBackgroundSubtractorMOG2(varThreshold=8, history=200)
    else:
        backSub = cv.createBackgroundSubtractorKNN(history=100)
    
    # get video from vsrc
    capture = cv.VideoCapture(vsrc)
    # check if video can be opened
    if not capture.isOpened():
        print('Unable to open: ' + vsrc)
        exit(0)
    # play video by frame by frame
    while True:
        # read frame from capture obj
        ret, frame = capture.read()
        if frame is None:
            break
        
        # apply background subtrcation algorythm on frame
        fgMask = backSub.apply(frame, learningRate=-1)

        # check if there is any motion in the frame
        if is_oqqupied(fgMask, 1):

            # if theres any motion, draw green border around the frame
            border = cv.copyMakeBorder(frame, 10,10,10,10,cv.BORDER_CONSTANT, value=GREEN)

            if sensAlgo == 'tm':

                # applying the motion tracker module
                x,y,w,h = track_motion(frame, fgMask)

                # drawing border around detected motion
                border = cv.rectangle(border, (x, y), (x+w, y+h), 255, 2)
            if sensAlgo == 'tm2':

                # apply canny algorythm
                fgMask = track_motion2(border, fgMask)
        else:

            # if theres no motion, draw red border around the frame
            border = cv.copyMakeBorder(frame, 10,10,10,10,cv.BORDER_CONSTANT, value=RED)


        # cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
        # cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
        #             cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
        
        # edges = cv.Canny(fgMask, 127, 255)

        # show frames with imshow
        # cv.imshow('Canny', edges)
        cv.imshow('Frame', border)
        cv.imshow('FG Mask', fgMask)
        
        # waiting for exit key, which in this case is 'Q'
        if cv.waitKey(1) == ord('q'):
            break

if __name__ == '__main__':
    bgsub(0, 'MOG2')