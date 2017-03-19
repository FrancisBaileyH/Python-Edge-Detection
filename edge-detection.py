from PIL import Image
import sys
import getopt
import numpy
from ConvolutionStrategy import ConvolutionStrategy
from SobelOperatorStrategy import SobelOperatorStrategy
from KirschOperatorStrategy import KirschOperatorStrategy
from PrewittOperatorStrategy import PrewittOperatorStrategy
from GenericBlurStrategy import GenericBlurStrategy


operations = {
    "sobel": SobelOperatorStrategy(),
    "kirsch": KirschOperatorStrategy(),
    "prewitt": PrewittOperatorStrategy(),
    "blur": GenericBlurStrategy()
}


#
# Setup the expected command line arguments
# and validate what we received.
#
def main(argv):

    mask = None
    filename = None
    help_text = 'edge-detection.py -m <mask> -i <image>'

    try:
        opts, args = getopt.getopt(argv, "hm:i:", ["mask=", "image="])
    except getopt.GetoptError, _:
        print help_text
        sys.exit(2)

    for opt, arg in opts:

        if opt == '-h':
            print help_text
            sys.exit()
        elif opt in ('-m', '--mask'):
            mask = arg
        elif opt in ('-i', '--image'):
            filename = arg

    if mask is None or filename is None:
        print help_text
        sys.exit(2)

    if mask not in operations.keys():
        print "Unknown mask: " + mask
        sys.exit(2)

    run(mask, filename)


#
# Run the given mask against our image file
#
def run(mask, filename):

    print "Running..."

    try:

        image = Image.open(filename)
        image = image.convert('L')

        pixels = numpy.fromstring(image.tobytes(), dtype=numpy.uint8)
        pixels = pixels.reshape((image.size[1], image.size[0]))

        operator = operations[mask]
        pixel_values = None

        if isinstance(operator, ConvolutionStrategy):
            pixels = operations["blur"].mask(pixels)
            gradients, g_min, g_max = operator.mask(pixels)
            pixel_values = operator.normalize_pixel_values(gradients, g_min, g_max)

        else:
            pixel_values = operator.mask(pixels)

        visualize(image, pixel_values)

    except RuntimeError, e:
        print e


#
# Visualize the results
#
def visualize(image, pixel_values):

    print "Visualizing..."
    width, height = image.size

    # Visualize the gradients
    for y in range(0, height):

        for x in range(0, width):
            image.putpixel((x, y), pixel_values[y][x])

    image.show()


if __name__ == "__main__":
    main(sys.argv[1:])
