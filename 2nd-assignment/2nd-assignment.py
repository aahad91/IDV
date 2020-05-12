"""
Using one slice of a CT angiographic scan:
(a) Draw a profile line through line 256 of this 2D data set.
(b) Calculate the mean value and the variance value of this 2D data set.
(c) Display a histogram of this 2D data set (instead of bars you may use a line
graph to link occurrences along the x-axis).
(d) Rescale values to range between 0 and 255 using a linear transformation.
(e) Rescale values to range between 0 and 255 using a different
(e.g. non-linear) transformation.
(f) Use an 11x11 boxcar smoothing filter on the 2D data set.
(g) Use an 11x11 median filter on the 2D data set.

Name: Abdul Ahad Ayaz
"""
# ---packages--- #
import numpy as np
import math
import matplotlib.pyplot as plt
import struct
# ---Task Functions--- #
# def profile_line():

# def mean1():

# def variance1():

# def calc_histogram():

# def linear_transform():

# def nonlinear_transform():

# def boxcar_filter():

# def median_filter():

# def visual():

# ----------------------------------#
if __name__ == "__main__":
    with open('slice150.raw', 'rb') as raw:
        r_data = raw.read(2)        # reading 2bytes of data 
        print(r_data)
