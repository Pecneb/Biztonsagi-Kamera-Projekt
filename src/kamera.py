import matplotlib.pyplot as plt
import numpy
import cv2 as cv

'''
this module gets video srouce as input,
then shows the kamera or play the video
'''
def kamera():
    # getting video source
    cap = cv.VideoCapture(0)
    
    # generating warning message if couldnt open video
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
        
    # showing video, frame by frame
    while True:
        ret, frame = cap.read()
        
        # checking if theres any frames recieved
        if not ret:
            print("Cant recieve frame (stream end?). Exiting ...")
            break
        
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # showing frame
        cv.imshow('frame', frame)
        
        # waiting for exit key, which in this case is 'Q'
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    kamera()