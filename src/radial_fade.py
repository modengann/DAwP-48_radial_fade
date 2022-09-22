#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    pass

def radial_distance(a):
    pass

def scale(a, tmin=0.0, tmax=1.0):
    pass

def radial_mask(a):
    pass

def radial_fade(a):
    pass

def main():
    image = plt.imread("src/painting.png").copy()
    f, ax = plt.subplots(3,1)
    ax[0].imshow(image)
    ax[1].imshow(radial_mask(image))
    ax[2].imshow(radial_fade(image))
    plt.show()

if __name__ == "__main__":
    main()
