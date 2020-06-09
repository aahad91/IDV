"""

Name: Abdul Ahad Ayaz
"""
# ---packages--- #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas.plotting as pp
import seaborn as sns
# ---Task Functions--- #

# ----------------------------------#


if __name__ == "__main__":
    # --- Reading Data--- #
    data = pd.read_csv('DataWeierstrass.csv', delimiter=';')
    # ---Scatter Matrix--- #
    sm = sns.pairplot(data, hue='professor', kind='scatter', diag_kind='None', height=2, aspect=2, markers='+')
    for ax in sm.axes.flat:
        plt.setp(ax.get_xticklabels(), rotation=0)

    # ---Parallel Cooedinates--- #

    plt.show()
