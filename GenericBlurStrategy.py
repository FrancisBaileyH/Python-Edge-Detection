from BlurStrategy import BlurStrategy


class GenericBlurStrategy(BlurStrategy):

    def mask_pixel(self, x, y, pixels):

        g = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]

        pixel_value = (
            g[0][0] * self.get_pixel_safe(pixels, x - 1, y - 1, None) +
            g[0][1] * self.get_pixel_safe(pixels, x, y - 1, None) +
            g[0][2] * self.get_pixel_safe(pixels, x + 1, y - 1, None) +
            g[1][0] * self.get_pixel_safe(pixels, x, y - 1, None) +
            g[1][1] * self.get_pixel_safe(pixels, x, y, None) +
            g[1][2] * self.get_pixel_safe(pixels, x, y + 1, None) +
            g[2][0] * self.get_pixel_safe(pixels, x - 1, y + 1, None) +
            g[2][1] * self.get_pixel_safe(pixels, x, y + 1, None) +
            g[2][2] * self.get_pixel_safe(pixels, x + 1, y + 1, None)
        )

        return int(pixel_value / 9)
