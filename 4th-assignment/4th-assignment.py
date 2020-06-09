"""

Name: Abdul Ahad Ayaz
"""
# ---packages--- #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas.plotting as pp
import seaborn as sns
# ---Task Functions--- #

# ----------------------------------#


if __name__ == "__main__":
    # --- Reading Data--- #
    data = pd.read_csv('DataWeierstrass.csv', delimiter=';')
    data1 = data.iloc[:, 2:]
    print(data1.head())
    pp.scatter_matrix(data1, diagonal='kde')
    #sns.pairplot(data1, kind='scatter')
    plt.show()
