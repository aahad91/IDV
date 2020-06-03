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
    return prof_line


def histo_line(data):
    pixel, count = np.unique(data, return_counts=True)
    hist = dict(zip(pixel, count))
    return hist


def rescale_val(data):
    i_max = max_val(data)
    i_min = min_val(data)
    tf = np.zeros([len(data), len(data)])
    for x in range(0, len(data)):
        for y in range(0, len(data)):
            i = data[x][y]
            tf[x][y] = (((i - i_min) / (i_max - i_min))*255)
    return tf


def histo_eq(data, rscale):
    maxval = rscale
    val = histo_line(data)
    cdf = {}
    sum = 0
    h_equ = np.zeros([len(data), len(data)])
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


def color_transform(r, g, b):
    scale = 255
    r_equ = histo_eq(r, scale)
    g_equ = histo_eq(g, scale)
    b_equ = histo_eq(b, scale)
    color_tf = np.empty([len(b), len(b), 3])
    for x in range(0, len(r)):
        for y in range(0, len(r)):
            val = np.array([r_equ[x][y], g_equ[x][y], b_equ[x][y]])
            color_tf[x][y] = val
    color_tf = color_tf.astype('int64')
    return color_tf


def visual(band1, band2, band3, band4):
    fig, axs = plt.subplots(2, 4, figsize=(18, 8), constrained_layout=True)
    axs[0, 0].plot(prof_line_max(band2))
    axs[0, 0].set_title('Profile Line')
    axs[0, 1].plot(list(histo_line(band2).values()))
    axs[0, 1].set_title('Histogram-Band2')
    axss = axs[0, 2].imshow(rescale_val(band2), 'gray')
    axs[0, 2].set_title('Rescaling(Max/Min) - Linear Transform')
    fig.colorbar(axss, ax=axs[0, 2], ticks=[np.min(rescale_val(band2)), np.max(rescale_val(band2))])
    axs[0, 3].imshow(histo_eq(band1, max_val(band1)), 'gray')
    axs[0, 3].set_title('Histogram Equalization-Band1')
    axs[1, 0].imshow(histo_eq(band2, max_val(band2)), 'gray')
    axs[1, 0].set_title('Histogram Equalization-Band2')
    axs[1, 1].imshow(histo_eq(band3, max_val(band3)), 'gray')
    axs[1, 1].set_title('Histogram Equalization-Band3')
    axs[1, 2].imshow(histo_eq(band4, max_val(band4)), 'gray')
    axs[1, 2].set_title('Histogram Equalization-Band4')
    axs[1, 3].imshow(color_transform(band4, band3, band1))
    axs[1, 3].set_title('Color Transformation')
    fig.suptitle('Space Imaging')
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

    # ---Plotting --- #
    visual(band1, band2, band3, band4)
