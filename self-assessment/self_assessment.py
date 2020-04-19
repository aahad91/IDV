import matplotlib.pyplot as plt
import numpy as np
from array import array

elevation = array('B')

with open('colorado_elev.vit', 'rb') as data:
    header = data.read(268)
    elevation.fromfile(data, 160000)
    file_size = data.tell()
print("File Size:", file_size)

array = np.array(elevation)
array2d = array.reshape(400, 400)
print(array2d.shape)

fig, axarr = plt.subplots(2, 2)
axarr[0, 0].imshow(array2d, cmap='terrain')
axarr[0, 1].imshow(array2d, cmap='hsv')
axarr[1, 0].imshow(array2d, cmap='gray')
axarr[1, 1].plot(array2d[100], label ='line 100')
axarr[1, 1].plot(array2d[200], label ='line 200')
axarr[1, 1].plot(array2d[300], label ='line 300')
axarr[1, 1].set(xlabel='pixels', ylabel='elevation')
plt.show()
