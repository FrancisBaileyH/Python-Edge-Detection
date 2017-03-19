from MaskStrategy import MaskStrategy


#
# Abstract class for kernel convolution operations
#
class BlurStrategy(MaskStrategy):

    #
    #  Loop through all pixels and run the
    #  mask_pixel template method
    #
    def mask(self, pixels):

        height = len(pixels)
        width = len(pixels[0])

        blur_values = [[0 for x in range(width)] for y in range(height)]

        for y in range(0, height):

            for x in range(0, width):
                blur_values[y][x] = self.mask_pixel(x, y, pixels)

        return blur_values
