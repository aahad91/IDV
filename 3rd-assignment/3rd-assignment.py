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
    plt.show()
    print(pline[0])
# def histo_line():
# def rescale_val():
# def histo_eq():
# def color_transform():
# ----------------------------------#


if __name__ == "__main__":

    raw2 = pd.read_csv('orion/i170b2h0_t0.txt', header=None)
    df = raw2.to_numpy()
    band2 = np.flip(df, 0)
    print(df)
    print('\n')
    print(band2)
    #plt.imshow(band2, cmap='gray')
    #plt.show()
    print("Max Value:", max_val(band2))
    print("Min Value:", min_val(band2))
    print("Mean:", mean_val(band2))
    print("Variance:", var_val(band2))
    prof_line_max(band2)
