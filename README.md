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
  - `track_motion2.py`
      - Implements motion tracking another way.

## User guide:

```
usage: main.py [-h] [--input INPUT] [--bsAlgo BSALGO] [--sensAlgo SENSALGO]

Security Camera with motion detection.(quit with 'q')

optional arguments:
  -h, --help           show this help message and exit
  --input INPUT        path to the video source (webcam is default).
  --bsAlgo BSALGO      Choose the background subtraction algorythm MOG2 or KNN
  --sensAlgo SENSALGO  Choose what type of motion detection to use: tm or tm2. tm is for less populated areas, tm2 is
                       more stable

```
