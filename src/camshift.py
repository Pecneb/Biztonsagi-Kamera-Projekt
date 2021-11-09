from typing import Annotated
import cv2 as cv

def track_motion(frame, mask, initial_track_window = ()):
    '''
    This module takes frame and mask arguments.
    Frame is a frame from a video src.
    The mask is the area of a motion on the video frame.
    From these information, the module will track the object on the screen.
    And it will return the position of the sensed motion.
    x,y coordinates with w=width, h=height
    '''
    # initialize location of tracking window
    x, y, w, h = initial_track_window
    track_window = (x, y, w, h)

    # prepare frame
    img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)


    # calc hist 
    mhist = cv.calcHist([img], [0], None, [2], [0,256])
    
    # range of interest
    roi = img[y:y+h, x:x+w]
    term_crit =( cv.TERM_CRITERIA_EPS | cv.TermCriteria_COUNT, 10, 1)

    # calc backproject
    dst = cv.calcBackProject([img], [0], mhist, [10,255], 1)
    
    # apply meanshift for object tracking
    # it gives back the tracking window parameters
    ret, new_position_of_object = cv.CamShift(dst, track_window, term_crit)
    x, y, w, h = new_position_of_object
    
    return x,y,w,h



