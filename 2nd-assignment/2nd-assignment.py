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


def profile_line(data):
    array2d = data.reshape(512, 512)
    prof_line = []
    for i in range(0, 512):
        prof_line.append(array2d[i, 255])
    plt.plot(prof_line)
    plt.title('256 Profile Line')
    plt.show()


def mean1(data):
    mean = sum(data)/len(data)
    print(mean)


def variance1(data):
    var = np.var(data)
    print(var)


def plot_histogram(data):

    plt.hist(data, histtype='step')
    plt.show()


def linear_transform(data):
    i_max = 0
    i_min = 0
    linear_tf = [None]*len(data)
    for x in range(0, len(data)):
        i = data[x]
        if i_max is None or i_max < i:
            i_max = i
        if i_min is None or i_min > i:
            i_min = i
        linear_tf[x] = ((i - i_min) / (i_max - i_min))*255
    linear_tf = np.asarray(linear_tf)
    pixel = linear_tf.reshape(512, 512)
    plt.imshow(pixel)
    plt.show()



def nonlinear_transform(data):
    nlinear_tf =[None]*len(data)
    for y in range(0, len(data)):
        px = data[y]
        nlinear_tf[y] = math.log2(px + 1)
    nlinear_tf = np.asarray(nlinear_tf)
    pixel = nlinear_tf.reshape(512, 512)
    plt.imshow(pixel, 'gray')
    plt.show()

# def boxcar_filter():

# def median_filter():

# def visual():

# ----------------------------------#


if __name__ == "__main__":
    raw = np.fromfile('slice150.raw', dtype='int16')
    mean1(raw)
    variance1(raw)
    #profile_line(raw)
    #plt_histogram(raw)
    #linear_transform(raw)
    #print(len(raw))
    #print(array2d)
    nonlinear_transform(raw)
    #test(raw)
    #print(type(raw))
