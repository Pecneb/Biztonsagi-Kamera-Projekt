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
  - `bgsub.py`
      - This module uses background subtraction to show motion.
  - `occipation.py`
      - This module helps with detecting motion.
  - `track_motion.py`
      - Tracks motion, using CamShift algorythm.
  - `track_motion2.py`
      - Tracks motion using contour detection.

## User guide:

```
usage: main.py [-h] [--input INPUT] [--bsAlgo BSALGO] [--sensAlgo SENSALGO]

Security Camera with motion detection.(quit with 'q')

optional arguments:
  -h, --help           show this help message and exit
  --input INPUT        path to the video source (webcam is default).
  --bsAlgo BSALGO      Choose the background subtraction algorythm MOG2 or KNN (MOG2 is default)
  --sensAlgo SENSALGO  Choose what type of motion detection to use: tm or tm2. tm is for less populated areas, tm2 is more stable (tm2 is default)

```
