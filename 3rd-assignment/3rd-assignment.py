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
            if v in cdf.keys():
                h_equ[x][y] = cdf.get(v)
    return h_equ


# def color_transform():
def visual(band1, band2, band3, band4):
    fig, axs = plt.subplots(2, 2, figsize=(10, 10), constrained_layout=True)
    axs[0, 0].imshow(histo_eq(band1), 'gray')
    axs[0, 0].set_title('Band1')
    axs[0, 1].imshow(histo_eq(band2), 'gray')
    axs[0, 1].set_title('Band2')
    axs[1, 0].imshow(histo_eq(band3), 'gray')
    axs[1, 0].set_title('Band3')
    axs[1, 1].imshow(histo_eq(band4), 'gray')
    axs[1, 1].set_title('Band4')
    plt.savefig('space_imaging.jpeg', dpi=200)
    plt.show()
# ----------------------------------#


if __name__ == "__main__":

    # --- Reading Data--- #
    raw1 = pd.read_csv('orion/i170b1h0_t0.txt', header=None)
    df1 = raw1.to_numpy()
    band1 = np.flip(df1, 0)
    raw2 = pd.read_csv('orion/i170b2h0_t0.txt', header=None)
    df2 = raw2.to_numpy()
    band2 = np.flip(df2, 0)
    raw3 = pd.read_csv('orion/i170b3h0_t0.txt', header=None)
    df3 = raw3.to_numpy()
    band3 = np.flip(df3, 0)
    raw4 = pd.read_csv('orion/i170b4h0_t0.txt', header=None)
    df4 = raw4.to_numpy()
    band4 = np.flip(df4, 0)

    print("Max Value:", max_val(band2))
    print("Min Value:", min_val(band2))
    print("Mean:", mean_val(band2))
    print("Variance:", var_val(band2))

    # ---Plotting Histogram Equalization--- #
    visual(band1, band2, band3, band4)
