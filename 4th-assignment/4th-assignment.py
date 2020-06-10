"""

Name: Abdul Ahad Ayaz
"""
# ---packages--- #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.offline import plot


# --- Task Functions--- #
def scatter_matrix(data):
    sm = sns.pairplot(data, hue='professor', kind='scatter', diag_kind='None', height=2, aspect=2, markers='+')
    for ax in sm.axes.flat:
        plt.setp(ax.get_xticklabels(), rotation=0)
    plt.subplots_adjust(top=0.95)
    sm.fig.suptitle('Best Teacher Visualization: Scatter Matrix', fontsize=16)
    plt.savefig('scatter_matrix.jpeg', dpi=200)


def parallel_coordinate(data):
    u, data['professor1'] = np.unique(data['professor'], return_inverse=True)
    v, data['lecture1'] = np.unique(data['lecture'], return_inverse=True)
    data1 = data.drop(['professor', 'lecture'], axis=1)
    for i in data1.index:
        data1.at[i, 'professor1'] += 1
        data1.at[i, 'lecture1'] += 1

    pc = px.parallel_coordinates(data1[['professor1', 'lecture1', 'participants', 'professional expertise',
                                        'motivation', 'clear presentation', 'overall impression']], color='professor1',
                                        labels={'professor1': 'professor', 'lecture1': 'lecture'},
                                        color_continuous_scale=px.colors.cyclical.mrybm,
                                        title='Best Teacher Visualization: Parallel Coordinates')
    plot(pc, filename='parallel_coordinate.html')
    return pc


# ----------------------------------#
if __name__ == "__main__":

    # --- Reading Data--- #
    data = pd.read_csv('DataWeierstrass.csv', delimiter=';')

    scatter_matrix(data)
    parallel_coordinate(data).show()
    plt.show()
