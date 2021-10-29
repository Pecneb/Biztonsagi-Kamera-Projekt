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

def updateObjects(updaterate, framecount, objectHistograms = [], updatedHistograms = []):
    '''
    Update obj array depending on updaterate and framcount.
    If the same obj hist is found on frame, then update obj position.
    '''
    if (framecount%updaterate)==0:
        for oh in range(len(objectHistograms)):
            # compare histograms, to find best match
            bestMatch = 0.00
            iofhist = oh
            for uh in range(len(updatedHistograms)):
                if uh <= oh:
                    match = cv.compareHist(objectHistograms[oh][0], updatedHistograms[uh][0], 1)
                    if bestMatch > match:
                        bestMatch = match
                        iofhist = uh
                else:
                    objectHistograms.append(updatedHistograms[uh])
            print(bestMatch)
            if bestMatch != 0.0:
                objectHistograms.remove(objectHistograms[oh])
            
        
def camshiftOnObjects(frame, objectHistograms=[]):
    term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    for obj in objectHistograms:
        track_window = obj[1]
        dst = cv.calcBackProject([hsv], [0], obj[0], [0,180], 1)
        ret, track_window = cv.CamShift(dst, track_window, term_crit)
        x,y,w,h = track_window
        cv.rectangle(frame, (x,y), (x+w, y+h), 255, 2)

def track_motion2(frame, mask, updaterate, framecount, objectHistograms = []):
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
            newObjects.append([obj, (x,y,w,h)])

            # draw rectangle on original frame
            cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)

    # calculate the histograms of the given objects
    # newObjectHistograms = histOfObjects(newObjects)
    
    # camshiftOnObjects(frame, objectHistograms)

    # objectHistograms = newObjectHistograms

    # updateObjects(framecount, updaterate, objectHistograms, newObjectHistograms)
    
    # return finale mask image for debug purposes
    return morph, objectHistograms