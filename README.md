# Biztonsagi kamera:

Security camera with motion detection and tracking.  

Dependencies:
  - Python 3.9.7
  - OpenCV-Python
  - Numpy
  - Matplotlib.Pyplot
  - Argparse
  - os
  - sys
  
## Modules:
  
  - `main.py`
      - The software can be started with the `main.py` file, that takes additional arguments.  
  - `kamera.py`
      - The module can open videos or live camera feed, with the given source path.
  - `bgsub.py`
      - This module uses background subtraction to show motion.
  - `occipation.py`
      - This module helps with detecting motion.
  - `track_motion.py`
      - This module tracks the detected motion.

## User guide:

```
python main.py -h
usage: main.py [-h] [--mode MODE] [--algo ALGO] [video source path]

Security Camera with motion detection.(quit with 'q')

positional arguments:
  [video source path]  path to the video source (0 to use webcam).

optional arguments:
  -h, --help           show this help message and exit
  --mode MODE          Choose: show camera/video (play) or background subtraction (md) mode.
  --algo ALGO          Choose what background subtractor algo to use: MOG2 or KNN

```
