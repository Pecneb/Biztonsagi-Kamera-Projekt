import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

'''
Tells if there motion in the frame or not.
'''
def is_oqqupied(frame, threshold):
    '''
    Frame: the input image, this should be a foreground mask
    Threshold: with this argument, we can adjust the sensitivity of the detection in range 0 - 10000.
        the smaller the number, the smaller motion can be detected. 
    '''
    # img = cv.imread('./Back_Projection_Theory0.jpg')
    
    #calculate histogram of the image
    hist = cv.calcHist([frame], [0], None, [2], [0,256])
    
    # plt.figure()
    # plt.title("Hist")
    # plt.xlabel("Bins")
    # plt.ylabel("number of pixels")
    # plt.plot(hist)
    # plt.xlim([0,256])
    # plt.show()
    
    summa = sum(hist[:,0])
    
    # print(hist[1])
    # print(f"Over 50: {oth0} \t Under 50: {uth1} And {summa}")
    
    if (hist[1]/summa)*10000 > threshold:
        return True
    return False

if __name__ == '__main__':
    is_oqqupied()