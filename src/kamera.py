import matplotlib.pyplot as plt
import numpy
import cv2

'''
this module gets video srouce as input,
then shows the kamera or play the video with GUI
'''
def kamera(vsrc):
    # getting video source
    cap = cv2.VideoCapture(vsrc)
    
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
        
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # showing frame
        cv2.imshow('frame', frame)
        
        # waiting for exit key, which in this case is 'Q'
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    kamera()