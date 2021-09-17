import matplotlib.pyplot as plt
import numpy
import cv2

def kamera(vsrc):
    cap = cv2.VideoCapture(vsrc)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Cant recieve frame (stream end?). Exiting ...")
            break
        
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

