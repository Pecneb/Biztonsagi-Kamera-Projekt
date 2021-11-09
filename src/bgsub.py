import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from oqqupation import is_oqqupied
from camshift import track_motion
from track_object import track_motion2

GREEN = [0,255,0]
RED = [0,0,255]

def bgsub(vsrc, algo):
    '''
    Object motion sensing with Backgroundsubtraction.
    bgsub(vsrc, algo)
    vsrc = video source
    algo = background subtraction algorythm
    '''
    # choose what algorythm to use: MOG2 or KNN
    if algo == 'MOG2':
        backSub = cv.createBackgroundSubtractorMOG2(varThreshold=40)
    else:
        backSub = cv.createBackgroundSubtractorKNN()
    
    # get video from vsrc
    capture = cv.VideoCapture(vsrc)
    
    # check if video can be opened
    if not capture.isOpened():
        print('Unable to open: ' + vsrc)
        exit(0)

    vmask = None

    # play video by frame by frame
    while True:
        # read frame from capture obj
        ret, frame = capture.read()
        if frame is None:
            break

        # apply background subtrcation algorythm on frame
        fgMask = backSub.apply(frame, learningRate=-1)

        # check if there is any motion in the frame
        if is_oqqupied(fgMask, 10):
            # if theres any motion, draw green border around the frame
            border = cv.copyMakeBorder(frame, 10,10,10,10,cv.BORDER_CONSTANT, value=GREEN)            

            if vmask is None:
                vmask = np.zeros(border.shape, dtype=np.uint8)

            # contour finding algorythm
            fgMask, vmask = track_motion2(border, fgMask, vmask)
            vectors = cv.add(border, vmask)
            cv.imshow('Drawn vectors',vectors)
        else:
            # if theres no motion, draw red border around the frame
            border = cv.copyMakeBorder(frame, 10,10,10,10,cv.BORDER_CONSTANT, value=RED)


        # cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
        # cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
        #             cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
        
        # show frames with imshow
        cv.imshow('Original Frame', border)
        cv.imshow('Foreground mask', fgMask)
        
        # waiting for exit key, which in this case is 'Q'
        if cv.waitKey(1) == ord('q'):
            break

if __name__ == '__main__':
    bgsub(0, 'MOG2')