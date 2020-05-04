"""
This program shows water flowing through a channel. Winds acting upon
the (open) surface of the water create turbulences inside the water. Movements
of water particles (caused by winds) were calculated by students in the first
supercomputing class by Prof. Lloyd Fosdick, University of Colorado, 1992.
File “field2.irreg” contains data describing the particle movement in 2d slide
perpendicular to the length of the channel. Data is given for a regular 82x82
grid in following format:starting position(x,y,z) and relative movement(u,v,w).

Name: Abdul Ahad Ayaz
"""
# Used Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# Data Cleaning
da = pd.read_csv('field2.irreg')
db = da.drop([0, 1, 2, 3, 4])

# Data formatting
db.columns = ['Data']
db[['x', 'y', 'z', 'u', 'v', 'w']] = db.Data.str.split(expand=True)
db.drop(columns=['Data'], inplace=True)
db.to_csv('test.csv')

# Plotting Datapoints
flow_data = pd.read_csv('test.csv')
flow_plt = plt.subplots(dpi=200)
normc = colors.Normalize(vmin=0, vmax=1)
for index, row in flow_data.iterrows():     # looping throught rows of data
    clr = np.hypot(row.u, row.v)            # calculating color value
    flow_plt = plt.quiver(row.x, row.y, row.u, row.v, clr, cmap='jet',
                        norm=normc, scale=5, width=0.001, headlength=8,
                        headwidth=8, pivot='mid')

# Colorbar setting
clb = plt.colorbar(flow_plt, ticks=[0, 0.5, 1])
clb.set_ticklabels(['Low', 'Medium', 'High'])
clb.set_label('Flow Velocity', rotation=90)

# Plot labeling
plt.title('Vector Field Visualization')
plt.xlabel('X Equivalent of Vectors')
plt.ylabel('Y Equivalent of Vectors')
plt.savefig('vector_field.jpeg', dpi=200)
plt.show()
