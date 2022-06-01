import cv2 as cv

def record_video(frames, width, height, outname):
    fourcc = cv.videoWriter_fourcc(*'XVID')
    out = cv.VideoWriter(outname, fourcc, 20.00, (width, height))

    for frame in frames:
        out.write(frame)

    out.release()
