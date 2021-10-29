import cv2 as cv
import numpy

def find_rois(frame, mask, rois = []):
    # Remove noice
    blur = cv.GaussianBlur(mask, (9,9), 0)
    
    # Remove false positives, with threshold
    _, thresh = cv.threshold(blur, 160, 255, cv.THRESH_BINARY)
    
    # Enhance moving object
    morph = cv.morphologyEx(thresh, cv.MORPH_OPEN, None, iterations=3)
    # morph = cv.morphologyEx(morph, cv.MORPH_CLOSE, None, iterations=3)
    morph = cv.dilate(thresh, None, iterations=2)

    # Find objects with contour detection
    contours, hierarchy = cv.findContours(morph, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        roi = cv.boundingRect(contour)

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject()
