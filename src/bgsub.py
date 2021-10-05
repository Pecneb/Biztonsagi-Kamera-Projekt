import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from oqqupation import is_oqqupied
from track_motion import track_motion

GREEN = [0,255,0]
RED = [0,0,255]


'''
Background subtraction module
'''
def bgsub(vsrc, algo):
    
    if algo == 'MOG2':
        backSub = cv.createBackgroundSubtractorMOG2()
    else:
        backSub = cv.createBackgroundSubtractorKNN()
    capture = cv.VideoCapture(vsrc)
    if not capture.isOpened():
        print('Unable to open: ' + vsrc)
        exit(0)
    while True:
        ret, frame = capture.read()
        if frame is None:
            break
        
        fgMask = backSub.apply(frame, learningRate=-1)
        bgIm = backSub.getBackgroundImage()
        # blurring mask image, to decrease noice
        fgMask = cv.GaussianBlur(fgMask,(21,21), 0)

        if is_oqqupied(fgMask, 1):
            border = cv.copyMakeBorder(frame, 10,10,10,10,cv.BORDER_CONSTANT, value=GREEN)
            # applying the motion tracker module
            x,y,w,h = track_motion(frame, fgMask)
            # drawing border around detected motion
            border = cv.rectangle(border, (x, y), (x+w, y+h), 255, 2)
        else:
            border = cv.copyMakeBorder(frame, 10,10,10,10,cv.BORDER_CONSTANT, value=RED)

    
        cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
        cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
                    cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
        
        
        cv.imshow('Frame', border)
        cv.imshow('FG Mask', fgMask)
        
        # waiting for exit key, which in this case is 'Q'
        if cv.waitKey(1) == ord('q'):
            break

if __name__ == '__main__':
    bgsub(0, 'MOG2')