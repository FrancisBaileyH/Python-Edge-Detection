import math
from MaskStrategy import MaskStrategy


#
# Abstract class for kernel convolution operations
#
class ConvolutionStrategy(MaskStrategy):

    #
    #  Loop through all pixels and run the
    #   mask_pixel template method
    #
    def mask(self, pixels):

        height = len(pixels)
        width = len(pixels[0])

        gradient_magnitudes = [[0 for x in range(width)] for y in range(height)]
        gradient_max = None
        gradient_min = None

        for y in range(0, height):

            for x in range(0, width):

                gradient_magnitude = self.mask_pixel(x, y, pixels)

                if gradient_max is None:
                    gradient_max = gradient_magnitude
                    gradient_min = gradient_magnitude

                if gradient_magnitude > gradient_max:
                    gradient_max = gradient_magnitude

                if gradient_magnitude < gradient_min:
                    gradient_min = gradient_magnitude

                gradient_magnitudes[y][x] = gradient_magnitude

        return gradient_magnitudes, gradient_min, gradient_max

    #
    # Convert gradient values into 0 - 255 range
    #
    def normalize_pixel_values(self, gradient_magnitudes, g_min, g_max):

        height = len(gradient_magnitudes)
        width = len(gradient_magnitudes[0])

        # Visualize the gradients
        for y in range(0, height):

            for x in range(0, width):
                gradient_magnitude = gradient_magnitudes[y][x]
                gradient_magnitudes[y][x] = int(math.floor(255 * (gradient_magnitude - g_min) / (g_max - g_min)))

        return gradient_magnitudes

