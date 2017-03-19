import math

from ConvolutionStrategy import ConvolutionStrategy


class KirschOperatorStrategy(ConvolutionStrategy):

    #
    # Template method pattern, override mask function
    #
    def mask_pixel(self, x, y, pixels):

        gx = [
            [5, -3, -3],
            [5, 0, -3],
            [5, -3, -3]
        ]

        gy = [
            [5, 5, 5],
            [-3, 0, -3],
            [-3, -3, -3]
        ]

        gradient_y = (
            gy[0][0] * self.get_pixel_safe(pixels, x - 1, y - 1, None) +
            gy[0][1] * self.get_pixel_safe(pixels, x, y - 1, None) +
            gy[0][2] * self.get_pixel_safe(pixels, x + 1, y - 1, None) +
            gy[1][0] * self.get_pixel_safe(pixels, x, y - 1, None) +
            gy[1][2] * self.get_pixel_safe(pixels, x, y + 1, None) +
            gy[2][0] * self.get_pixel_safe(pixels, x - 1, y + 1, None) +
            gy[2][1] * self.get_pixel_safe(pixels, x, y + 1, None) +
            gy[2][2] * self.get_pixel_safe(pixels, x + 1, y + 1, None)
        )

        gradient_x = (
            gx[0][0] * self.get_pixel_safe(pixels, x - 1, y - 1, None) +
            gx[0][1] * self.get_pixel_safe(pixels, x, y - 1, None) +
            gx[0][2] * self.get_pixel_safe(pixels, x + 1, y - 1, None) +
            gx[1][0] * self.get_pixel_safe(pixels, x, y - 1, None) +
            gx[1][2] * self.get_pixel_safe(pixels, x, y + 1, None) +
            gx[2][0] * self.get_pixel_safe(pixels, x - 1, y + 1, None) +
            gx[2][1] * self.get_pixel_safe(pixels, x, y + 1, None) +
            gx[2][2] * self.get_pixel_safe(pixels, x + 1, y + 1, None)
        )

        return math.ceil(math.sqrt(pow(gradient_x, 2) + pow(gradient_y, 2)))
