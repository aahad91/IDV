import matplotlib.pyplot as plt
import matplotlib.colors as colors
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

elev = plt.subplot()
elev = plt.imshow(array2d, cmap='jet')
clb = plt.colorbar(elev, ticks=[5, 125, 255])
clb.set_ticklabels(['Low', 'Medium', 'High'])
clb.set_label('Elevation', rotation=90)
plt.title('Colorado Elevation')
plt.savefig('colorado_elev.jpeg', dpi=200)
plt.show()
