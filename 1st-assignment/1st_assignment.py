import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as colors
# data cleaning
da = pd.read_csv('field2.irreg')
db = da.drop([0, 1, 2, 3, 4])
db.columns = ['Data']
db[['x', 'y', 'z', 'u', 'v', 'w']] = db.Data.str.split(expand=True)
db.drop(columns=['Data'], inplace=True)
db.to_csv('test.csv')
# print(db.shape)
xc = pd.read_csv('test.csv')
# calculating the displacement
flow = plt.subplots(figsize=(10, 10))
for index, row in xc.iterrows():
    a = row.x + row.u
    b = row.y + row.v
    c = row.x - a
    d = row.y - b
    col = np.hypot(row.u, row.v)
    flow = plt.quiver(row.x, row.y, row.u, row.v, col, cmap='jet', norm=colors.Normalize(vmin=0, vmax=1), scale=4, width=0.001, headlength=10, headwidth=10)
    #ax.arrow(row.x, row.y, row.u, row.v, fc='white', ec='blue', head_length=0.009, head_width=0.007)
plt.show()
