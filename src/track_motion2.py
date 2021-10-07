import cv2 as cv

'''
In this module, i will implement motion tracking with contour detection and contour drawing.
'''
def track_motion2(frame, mask):
    '''
    Frame is the original frame of the captured video.
    Mask is the mask from the backgoundsubtraction. 
    '''
    
    
    # oframe = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(mask, (5,5), 0)
    _, thresh = cv.threshold(blur, 128, 255, cv.THRESH_BINARY)
    dilate = cv.dilate(thresh, None, iterations=3)
    contours, hierarchy = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # ret_img = cv.drawContours(frame, ret_img, -1, (0,0,255), 1)

    for contour in contours:
        (x,y,w,h) = cv.boundingRect(contour)
        print(cv.contourArea(contour))
        if cv.contourArea(contour) < 900:
            continue
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
