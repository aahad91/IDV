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
# Task A
def profile_line(data):
    array2d = data.reshape(512, 512)
    prof_line = []
    for i in range(0, 512):
        prof_line.append(array2d[255, i])
    return prof_line


# Task B
def mean1(data):
    mean = sum(data)/len(data)
    print("Mean:", mean)


# Task B
def variance1(data):
    var = np.var(data)
    print("Variance:", var)


# Task C
def plot_histogram(data):
    bin = np.bincount(data)
    return len(bin)


# Task D
def linear_transform(data):
    i_max = 0
    i_min = 0
    linear_tf = [None]*len(data)
    for x in range(0, len(data)):
        i = data[x]
        if i_max < i:
            i_max = i
        if i_min > i:
            i_min = i
        linear_tf[x] = ((i - i_min) / (i_max - i_min))*255
    linear_tf = np.asarray(linear_tf)
    pixel = linear_tf.reshape(512, 512)
    return pixel


# Task E
def nonlinear_transform(data):
    nlinear_tf = [None]*len(data)
    for y in range(0, len(data)):
        px = data[y]
        nlinear_tf[y] = math.log2(px + 1)
    nlinear_tf = np.asarray(nlinear_tf)
    pixel = nlinear_tf.reshape(512, 512)
    return pixel


# Task F
def boxcar_filter(data):
    filter = 11
    pad = filter // 2
    data = data.reshape(512, 512)
    row, col = data.shape
    for x in range(pad, row - (pad+pad)):
        for y in range(pad, col - (pad+pad)):
            filter_val = np.sum(data[x:filter + x, y:filter + y])*(1/121)
            data[x+5, y+5] = filter_val
    return data


# Task G
def median_filter(data):
    filter = 11
    pad = filter // 2
    data = data.reshape(512, 512)
    row, col = data.shape
    for x in range(pad, row - (pad+pad)):
        for y in range(pad, col - (pad+pad)):
            filter_val = np.sort(data[x:filter + x, y:filter + y], axis=None)
            val = filter_val[60]
            data[x+5, y+5] = val
    return data


def visual(data):
    fig, axs = plt.subplots(3, 2, figsize=(12, 10), constrained_layout=True)
    axs[0, 0].plot(profile_line(data))
    axs[0, 0].set_title('256 Profile Line')

    axs[0, 1].hist(data, bins=plot_histogram(data), histtype='step')
    axs[0, 1].set_title('Histogram')

    axs[1, 0].imshow(linear_transform(data), 'bone')
    axs[1, 0].set_title('Linear Transformation')

    axs[1, 1].imshow(nonlinear_transform(data), 'bone')
    axs[1, 1].set_title('Non-linear Transformation')

    axs[2, 0].imshow(boxcar_filter(data), 'bone')
    axs[2, 0].set_title('Boxcar Smoothing Filter')

    axs[2, 1].imshow(median_filter(data), 'bone')
    axs[2, 1].set_title('Median Filter')

    fig.suptitle('2d Spatial Data - Histogram, Transfer Functions, Filters')
    plt.savefig('medical_imaging.jpeg', dpi=200)
    plt.show()

# ----------------------------------#


if __name__ == "__main__":
    raw = np.fromfile('slice150.raw', dtype='int16')
    mean1(raw)
    variance1(raw)
    visual(raw)
