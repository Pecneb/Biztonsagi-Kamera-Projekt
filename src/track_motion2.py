import cv2 as cv

'''
In this module, i will implement motion tracking with contour detection and contour drawing.
'''
def track_motion2(frame, mask):
    '''
    Frame is the original frame of the captured video.
    Mask is the mask from the backgoundsubtraction. 
    '''
    
    # Remove noice
    blur = cv.GaussianBlur(mask, (9,9), 0)
    
    # Remove false positives, with threshold
    _, thresh = cv.threshold(blur, 200, 255, cv.THRESH_BINARY)
    
    # Enhance moving object
    dilate = cv.dilate(thresh, None, iterations=3)
    
    # Find objects with contour detection
    contours, hierarchy = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # ret_img = cv.drawContours(frame, ret_img, -1, (0,0,255), 1)

    # Iterate through objects, and draw rectangle around them
    for contour in contours:
        # get rectangle position
        (x,y,w,h) = cv.boundingRect(contour)
    
        # reduce motion noice
        if cv.contourArea(contour) > 300:
            # print contour area sizes for debug purposes
            print(cv.contourArea(contour))

            # draw rectangle on original frame
            cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)

    # return finale mask image for debug purposes
    return dilate