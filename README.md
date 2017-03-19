README
--------------------

Usage:

$ python2.7 edge-detection.py -m <sobel|kirsch|prewitt|blur> -i <image>

e.g.

$ python2.7 edge-detection.py -m kirsch -i ~/Downloads/test.jpg


Notes:

Only tested with python version 2.7. Currently only opens .jpg files.
The resulting output is a photo saved to the tmp directory and opened
with your systems image viewer. E.g. in linux it opens the image with
imagick.