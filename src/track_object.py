from typing import Match
import cv2 as cv

'''
In this module, i will implement motion tracking with contour detection and contour drawing.
'''

def histOfObjects(objects = []) :
    '''
    Calculate the histograms of input objects. 
    '''
    objHists = []

    for obj in objects:
        hsv_obj = cv.cvtColor(obj[0], cv.COLOR_BGR2HSV)
        objHist = cv.calcHist([hsv_obj], [0], None, [180], [0, 180])
        cv.normalize(objHist, objHist, 0, 255, cv.NORM_MINMAX)
        objHists.append([objHist, obj[1]])

    return objHists

def track_motion2(frame, mask, vmask):
    '''
    Frame is the original frame of the captured video.  
    Mask is the mask from the backgoundsubtraction. 
    '''

    # Remove noice
    blur = cv.GaussianBlur(mask, (9,9), 0)

    # Remove false positives, with threshold
    _, thresh = cv.threshold(blur, 127, 255, cv.THRESH_BINARY)

    # Enhance moving object
    open = cv.morphologyEx(thresh, cv.MORPH_OPEN, None, iterations=2)
    close = cv.morphologyEx(open, cv.MORPH_CLOSE, None, iterations=6)
    dilate = cv.dilate(close, None, iterations=4)

    # Find objects with contour detection
    contours, hierarchy = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # cv.drawContours(mask, contours, -1, (0,255,0), 50, hierarchy=hierarchy, maxLevel=1)

    # Save objects coordinates int his array
    vectors = []

    # Iterate through objects, and draw rectangle around them
    for contour in contours:
        # get rectangle/object position
        (x,y,w,h) = cv.boundingRect(contour)

        # filter out noice
        if cv.contourArea(contour) > 300:
            # print contour area sizes for debug purposes
            # print(cv.contourArea(contour))
            
            # get obj and obj position from frame and add to newObject arr
            # obj = frame[y:y+h, x:x+w]
            # newObjects.append([obj, (x,y,w,h)])
            vectors.append([x,y,w,h])

            # draw rectangle on original frame
            cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
            # cv.circle(frame, (int(x+(w/2)), int(y+(h/2))), 5, 255, 2)

    # print out detected moving objects for debug purpouses
    print(len(vectors))

    # draw vectors on frame
    for v in vectors:
        cv.circle(vmask, (int(v[0]+(v[2]/2)), int(v[1]+(v[3]/2))), 1, 255, 5)


    # return finale mask image for debug purposes
    return dilate, vmask