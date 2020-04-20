import matplotlib.pyplot as plt
from matplotlib.pylab import imshow, jet, show, ion, pause
import numpy as np
from numba import jit


"""
Author: Hossein Sadeghi

Most of the code is taken from Numba's tutorial.
I simply added a plotting that allow you to pick a point and zoom using some ad-hoc codes.


"""

@jit
def mandel(x, y, max_iters):
    """
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a fixed number of iterations.
    """
    i = 0
    c = complex(x,y)
    z = 0.0j
    for _ in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) < 4:
            i += 1

    return i

@jit
def create_fractal(min_x, max_x, min_y, max_y, image, iters):
    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height
    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            color = mandel(real, imag, iters)
            image[y, x] = color

    return image

sc = 2
x0 = 0
y0 = 0
N = 500
while True:
    plt.cla()
    s = np.zeros((N, N))
    create_fractal(x0 - sc / 2, x0 + sc / 2, y0 - sc / 2, y0 + sc / 2, s, 2000)
    imshow(s)

    res = plt.ginput(1, timeout=np.inf)[0]
    i, j = res
    x0 = x0 + sc * (i - N / 2) / N
    y0 = y0 + sc * (j - N / 2) / N
    sc = sc / 50
    pause(0.0001)

