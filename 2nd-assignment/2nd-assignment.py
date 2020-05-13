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

# ---Task Functions--- #


def profile_line(data_2d):
    prof_line = []
    for i in range(0, 512):
        prof_line.append(data_2d[i, 255])
    plt.plot(prof_line)
    plt.title('256 Profile Line')
    plt.show()


def mean1(data):
    mean = sum(data)/len(data)
    print(mean)


def variance1(data):
    # var = sum([(x - mean1(data))**2 for x in data]) / (len(data) - 1)
    var = np.var(data)
    print(var)


def calc_histogram(data_2d):
    plt.hist(data_2d, )
    #plt.show()
# def linear_transform():

# def nonlinear_transform():

# def boxcar_filter():

# def median_filter():

# def visual():

# ----------------------------------#


if __name__ == "__main__":
    raw = np.fromfile('slice150.raw', dtype='int16')
    mean1(raw)
    variance1(raw)
    array2d = raw.reshape(512, 512)
    profile_line(array2d)
    calc_histogram(array2d)
