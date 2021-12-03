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

    # vmask = None

    # params for ShoTomasi corner detection
    feature_params = dict( maxCorners = 100,
                           qualityLevel = 0.3,
                           minDistance = 7,
                           blockSize = 7 )
    
    # params for lucas kanade optical flow
    lk_params = dict( winSize = (15,15),
                      maxLevel = 2,
                      criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

    # create random colors
    color = np.random.randint(0, 255, (100,3))

    # mask image for drawing the vectors
    ret, frame_for_copy = capture.read()
    mask = np.zeros_like(cv.copyMakeBorder(frame_for_copy, 10,10,10,10,cv.BORDER_CONSTANT, value=RED))

    # play video by frame by frame
    while True:
        # read frame from capture obj
        ret, frame = capture.read()
        if frame is None:
            break

        # apply background subtrcation algorythm on frame
        fgMask = backSub.apply(frame, learningRate=-1)
        cv.imshow("Unprocessed FG", fgMask)
        
        # check if there is any motion in the frame
        if is_oqqupied(fgMask, 10):
            # if theres any motion, draw green border around the frame
            border = cv.copyMakeBorder(frame, 10,10,10,10,cv.BORDER_CONSTANT, value=GREEN)            

            # contour finding algorythm
            fgMask = track_motion2(border, fgMask)

            # find corners on first frame
            old_frame = frame
            old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
            p0 = cv.goodFeaturesToTrack(old_gray, mask = fgMask, **feature_params)

            # convert frame to gray
            frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            # ensuring opencv wont crash, calcOpticalFlow only when there are points to track
            if p0 is not None:
                # calculate optical flow
                p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
            
                # Select good points
                if p1 is not None:
                    good_new = p1[st==1]
                    good_old = p0[st==1]

                # draw vectors
                for i,(new,old) in enumerate(zip(good_new, good_old)):
                    a,b = new.ravel()
                    c,d = old.ravel()
                    mask = cv.line(mask, (int(a),int(b)), (int(c),int(d)), color[i].tolist(), 2)
                    frame = cv.circle(frame, (int(a),int(b)), 5, color[i].tolist(), -1)

                # Now update the previous frame and previous points
                old_gray = frame_gray.copy()
                p0 = good_new.reshape(-1,1,2)
            
            
        else:
            # if theres no motion, draw red border around the frame
            border = cv.copyMakeBorder(frame, 10,10,10,10,cv.BORDER_CONSTANT, value=RED)

        # Print frame number on frame
        cv.rectangle(border, (10, 2), (100,20), (255,255,255), -1)
        cv.putText(border, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
                    cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
        
        # show frames with imshow
        # making output image
        output = cv.add(border, mask)
        cv.imshow('Output', output)
        cv.imshow('Mask', fgMask)
        
        # waiting for exit key, which in this case is 'Q'
        if cv.waitKey(1) == ord('q'):
            break
        if cv.waitKey(1) == ord('p'):
            if cv.waitKey(0) == ord('p'):
                continue

if __name__ == '__main__':
    bgsub(0, 'MOG2')