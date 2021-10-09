from typing import Annotated
import cv2 as cv
from find_anomaly import find_anomaly

def track_motion(frame, mask):
    '''
    This module takes frame and mask arguments.
    Frame is a frame from a video src.
    The mask is the area of a motion on the video frame.
    From these information, the module will track the object on the screen.
    And it will return the position of the sensed motion.
    x,y coordinates with w=width, h=height
    '''
    # initialize location of tracking window
    x, y, w, h = 300, 200, 200, 120
    track_window = (x, y, w, h)

    # calc hist 
    mhist = cv.calcHist([mask], [0], None, [2], [0,256])
    
    # range of interest
    roi = mask[y:y+h, x:x+w]
    term_crit =( cv.TERM_CRITERIA_EPS | cv.TermCriteria_COUNT, 10, 1)

    # calc backproject
    dst = cv.calcBackProject([mask], [0], mhist, [10,255], 1)
    
    # apply meanshift for object tracking
    # it gives back the tracking window parameters
    ret, track_window = cv.CamShift(dst, track_window, term_crit)
    x, y, w, h = track_window
    
    return x,y,w,h



