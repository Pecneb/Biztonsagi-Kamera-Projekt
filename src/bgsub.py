import cv2 as cv

def bgsub(vsrc, algo):
    
    if algo == 'MOG2':
        backSub = cv.createBackgroundSubtractorMOG2()
    else:
        backSub = cv.createBackgroundSubtractorKNN()
    capture = cv.VideoCapture(vsrc)
    if not capture.isOpened():
        print('Unable to open: ' + args.input)
        exit(0)
    while True:
        ret, frame = capture.read()
        if frame is None:
            break
        
        fgMask = backSub.apply(frame)
        
        
        cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
        cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
                cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
        
        
        cv.imshow('Frame', frame)
        cv.imshow('FG Mask', fgMask)
        
        # waiting for exit key, which in this case is 'Q'
        if cv.waitKey(1) == ord('q'):
            break

if __name__ == '__main__':
    bgsub(0, 'MOG2')