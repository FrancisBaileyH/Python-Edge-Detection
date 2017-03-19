import math

from ConvolutionStrategy import ConvolutionStrategy


class PrewittOperatorStrategy(ConvolutionStrategy):

    #
    # Template method pattern, override mask function
    #
    def mask_pixel(self, x, y, pixels):

        gx = [
            [1, 0, -1],
            [1, 0, -1],
            [1, 0, -1]
        ]

        gy = [
            [1, 1, 1],
            [0, 0, 0],
            [-1, -1, -1]
        ]

        gradient_y = (
            gy[0][0] * self.get_pixel_safe(pixels, x - 1, y - 1, None) +
            gy[0][1] * self.get_pixel_safe(pixels, x, y - 1, None) +
            gy[0][2] * self.get_pixel_safe(pixels, x + 1, y - 1, None) +
            gy[2][0] * self.get_pixel_safe(pixels, x - 1, y + 1, None) +
            gy[2][1] * self.get_pixel_safe(pixels, x, y + 1, None) +
            gy[2][2] * self.get_pixel_safe(pixels, x + 1, y + 1, None)
        )

        gradient_x = (
            gx[0][0] * self.get_pixel_safe(pixels, x - 1, y - 1, None) +
            gx[0][2] * self.get_pixel_safe(pixels, x + 1, y - 1, None) +
            gx[1][0] * self.get_pixel_safe(pixels, x - 1, y, None) +
            gx[1][2] * self.get_pixel_safe(pixels, x + 1, y, None) +
            gx[2][0] * self.get_pixel_safe(pixels, x - 1, y - 1, None) +
            gx[2][2] * self.get_pixel_safe(pixels, x + 1, y + 1, None)
        )

        return math.ceil(math.sqrt(pow(gradient_x, 2) + pow(gradient_y, 2)))
