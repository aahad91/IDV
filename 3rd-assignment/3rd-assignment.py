"""

Name: Abdul Ahad Ayaz
"""
# ---packages--- #
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt


# ---Task Functions--- #
def max_val(data):
    return data.max()


def min_val(data):
    return data.min()


def mean_val(data):
    return data.mean()


def var_val(data):
    return data.var()


def prof_line_max(data):
    pline = np.where(data == data.max())
    prof_line = []
    for i in range(0, 500):
        prof_line.append(data[pline[0], i])
    plt.plot(prof_line)
    # plt.show()
    return prof_line
# def histo_line(data):


def rescale_val(data):
    # i_max = max_val(data)
    # i_min = min_val(data)
    tf = np.zeros([len(data), len(data)])
    for x in range(0, len(data)):
        for y in range(0, len(data)):
            i = data[x][y]
            tf[x][y] = math.log2(i + 1)
            # tf[x][y] = (((i - i_min) / (i_max - i_min))*255)
    print(np.shape(tf))
    plt.imshow(tf, cmap='gray')
    plt.show()
    return tf


def histo_eq(data):
    maxval = max_val(data)
    val = {}
    cdf = {}
    sum = 0
    h_equ = np.ones([len(data), len(data)])
    for x in range(0, len(data)):
        for y in range(0, len(data)):
            i = data[x][y]
            if i in val:
                val[i] += 1
            else:
                val[i] = 1
    for q, p in sorted(val.items()):
        pr = p/(500*500)
        sum += pr
        cdf[q] = round(sum*maxval)
    for x in range(0, len(data)):
        for y in range(0, len(data)):
            v = data[x][y]
            for key, value in cdf.items():
                if v == key:
                    h_equ[x][y] = value
    print(h_equ)
    plt.imshow(h_equ, 'gray')
    plt.show()


# def color_transform():
# ----------------------------------#


if __name__ == "__main__":

    raw2 = pd.read_csv('orion/i170b2h0_t0.txt', header=None)
    df = raw2.to_numpy()
    band2 = np.flip(df, 0)
    print(df)
    print('\n')
    # plt.imshow(band2, cmap='gray')
    # plt.show()
    print("Max Value:", max_val(band2))
    print("Min Value:", min_val(band2))
    print("Mean:", mean_val(band2))
    print("Variance:", var_val(band2))
    # prof_line_max(band2)
    # rescale_val(band2)
    histo_eq2(band2)
