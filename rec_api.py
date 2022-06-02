import cv2 as cv

def record_video(frames, width, height, outname):
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter(outname, fourcc, 20.00, (int(width), int(height)))

    for frame in frames:
        out.write(frame)

    out.release()
    print("Finished recording video.")
