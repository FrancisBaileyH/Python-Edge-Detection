class MaskStrategy(object):

    def mask(self, pixels):
        pass

    #
    # Template method for masking a single pixel, called by mask
    #
    def mask_pixel(self, x, y, pixels):
        pass

    #
    # Attempt to get a pixel at x and y, if the pixel
    # is out of bounds return a 0
    #
    def get_pixel_safe(self, image, x, y, layer):

        try:
            if layer is None:
                return image[y][x]
            else:
                return image[y][x][layer]

        except IndexError, _:
            return 0
