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

def updateObjects(objectHistograms = [], updatedHistograms = []):
    '''
    Update objects.
    '''
    retArr = []
    for i in range(len(objectHistograms)):
        match = 0.0
        found = i
        for j in range(len(updatedHistograms)):
            match = cv.compareHist(objectHistograms[i][0], updatedHistograms[j][0], 2)
            found = j
            if match == 0.0:
                retArr.append(i)
                break
        if match != 0.0:
            if found > i:
                retArr.append(updatedHistograms[found])
    if len(objectHistograms) == 0:
        retArr = updatedHistograms
    return retArr
        
def listObjects(objects = []):
    '''
    List found objects, only for debug.
    '''
    for o in objects:
        print(o[1])

def camshiftOnObjects(frame, objectHistograms=[]):
    term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    for obj in objectHistograms:
        track_window = obj[1]
        dst = cv.calcBackProject([hsv], [0], obj[0], [0,180], 1)
        ret, track_window = cv.CamShift(dst, track_window, term_crit)
        x,y,w,h = track_window
        cv.circle(frame, (int(x+(w/2)), int(y+(h/2))), 5, 255, 2)

def track_motion2(frame, mask, vectors = []):
    '''
    Frame is the original frame of the captured video.
    Mask is the mask from the backgoundsubtraction. 
    '''
    
    # Remove noice
    blur = cv.GaussianBlur(mask, (9,9), 0)
    
    # Remove false positives, with threshold
    _, thresh = cv.threshold(blur, 127, 255, cv.THRESH_BINARY)
    
    # Enhance moving object
    morph = cv.morphologyEx(thresh, cv.MORPH_OPEN, None, iterations=3)
    # morph = cv.morphologyEx(morph, cv.MORPH_CLOSE, None, iterations=3)
    morph = cv.dilate(thresh, None, iterations=1)

    # Find objects with contour detection
    contours, hierarchy = cv.findContours(morph, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(mask, contours, -1, (0,255,0), 50, hierarchy=hierarchy, maxLevel=1)

    # Save objects coordinates int his array
    newObjects = []

    # Iterate through objects, and draw rectangle around them
    for contour in contours:
        # get rectangle/object position
        (x,y,w,h) = cv.boundingRect(contour)

        # filter out noice
        if cv.contourArea(contour) > 500:
            # print contour area sizes for debug purposes
            # print(cv.contourArea(contour))
            
            # get obj and obj position from frame and add to newObject arr
            obj = frame[y:y+h, x:x+w]
            # newObjects.append([obj, (x,y,w,h)])
            vectors.append([x,y,w,h])

            # draw rectangle on original frame
            cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
            cv.circle(frame, (int(x+(w/2)), int(y+(h/2))), 5, 255, 2)
    
    # draw vectors on frame
    for v in vectors:
        cv.circle(frame, (int(v[0]+(v[2]/2)), int(v[1]+(v[3]/2))), 1, 255, 5)

    # return finale mask image for debug purposes
    return morph, vectors