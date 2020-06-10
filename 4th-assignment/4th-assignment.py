"""

Name: Abdul Ahad Ayaz
"""
# ---packages--- #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ----------------------------------#


if __name__ == "__main__":

    # --- Reading Data--- #
    data = pd.read_csv('DataWeierstrass.csv', delimiter=';')
    
    # ---Scatter Matrix--- #
    sm = sns.pairplot(data, hue='professor', kind='scatter', diag_kind='None', height=2, aspect=2, markers='+')
    for ax in sm.axes.flat:
        plt.setp(ax.get_xticklabels(), rotation=0)

    # ---Parallel Cooedinates--- #
    u, data['professor1'] = np.unique(data['professor'], return_inverse=True)
    v, data['lecture1'] = np.unique(data['lecture'], return_inverse=True)
    data1 = data.drop(['professor', 'lecture'], axis=1)
    for i in data1.index:
        data1.at[i, 'professor1'] += 1
        data1.at[i, 'lecture1'] += 1
    pc = px.parallel_coordinates(data1[['professor1', 'lecture1', 'participants', 'professional expertise',
                                        'motivation', 'clear presentation', 'overall impression']], color='professor1',
                                        labels={'professor1': 'professor', 'lecture1': 'lecture'},
                                        color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)
    pc.show()
    plt.show()
