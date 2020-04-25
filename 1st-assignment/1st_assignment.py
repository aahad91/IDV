import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm

# data cleaning
da = pd.read_csv('field2.irreg')
db = da.drop([0, 1, 2, 3, 4])
db.columns = ['Data']
db[['x', 'y', 'z', 'u', 'v', 'w']] = db.Data.str.split(expand=True)
db.drop(columns=['Data'], inplace=True)
print(db.shape)
# calculating the displacement
#for row in db.iterrows():
