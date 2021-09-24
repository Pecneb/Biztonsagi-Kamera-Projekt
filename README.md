# Biztonsagi kamera:

Egy python alapu mozgaserzekelo biztonsagi kamera, email ertesitessel.
A program elkeszitesehez a hasznalt konyvtarak:
    
  - OpenCV-Python
  - Numpy
  - Matplotlib.Pyplot
  - Argparse
  - os
  - sys
  
## Reszei:
  
  - `main.py`
      - progam main fajlja
  - `kamera.py`
      - video vagy kamera megjelenitese
  - `bgsub.py`
      - hatter kivonas, mozgaserzekeles
  - `occipation.py`
      - Igazat ad vissza, ha mozgas van a felvetelen

## Usage:

> ``main.py -h``
> ``usage: main.py [-h] [--mode MODE] [--algo ALGO] [video source path]``
>
> ``Security Camera with motion detection.(quit with 'q')``
>
>  ``positional arguments:``
>  ``[video source path]  path to the video source (0 to use webcam).``
>
> ``optional arguments:``
>  ``-h, --help           show this help message and exit``
>  ``--mode MODE          Choose: show camera/video (play) or background subtraction (md) mode.``
>  ``--algo ALGO          Choose what background subtractor algo to use: MOG2 or KNN``
