import numpy as np
import cv2 as cv
import os

def main():
    cap = cv.VideoCapture(os.path.join("B:", "opencv_test_video_dataset", "test_videos", "sherbrooke_video.avi"))

    # params for ShoTomasi corner detection
    feature_params = dict( maxCorners = 100,
                           qualityLevel = 0.3,
                           minDistance = 7,
                           blockSize = 7 )

    # params for lucas kanade optical flow
    lk_params = dict( winSize = (15,15),
                      maxLevel = 2,
                      criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

    # create random colors
    color = np.random.randint(0, 255, (100,3))

    # find corners on first frame
    ret, old_frame = cap.read()
    old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
    p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

    # mask image for drawing the vectors
    mask = np.zeros_like(old_frame)

    while (1):
        ret, frame = cap.read()
        if ret == None:
            break

        # convert frame to gray
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # calculate optical flow
        p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
        
        # Select good points
        if p1 is not None:
            good_new = p1[st==1]
            good_old = p0[st==1]

        # draw vectors
        for i,(new,old) in enumerate(zip(good_new, good_old)):
            a,b = new.ravel()
            c,d = old.ravel()
            mask = cv.line(mask, (int(a),int(b)), (int(c),int(d)), color[i].tolist(), 2)
            frame = cv.circle(frame, (int(a),int(b)), 5, color[i].tolist(), -1)
        img = cv.add(frame, mask)

        cv.imshow('Video', img)

        if cv.waitKey(30) == ord('q'):
            break
        
        # Update the previous frame and previous points
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1,1,2)

if __name__ == '__main__':
    main()