import cv2 as cv

def canny(img):
    '''
    Just experimenting with canny edge detection
    '''
    canny = cv.Canny(img, 127, 255)
    cv.imshow('Canny Image', canny)