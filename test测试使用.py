import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch

# Fixing random state for reproducibility
np.random.seed(19680801)
P_path='C:\\Users\\Jelly Jinzhe Liu\\Desktop\\Big-Project\\images\\背景.png'
w,h=500,500
# A sample image
with cbook.get_sample_data(P_path) as image_file:
    image = plt.imread(image_file)
    
plt.rcParams['savefig.dpi'] = 1 #分辨率
fig, ax = plt.subplots()
ax.imshow(image)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ax.axis('on')  # clear x-axis and y-axis
ax.set_title('CT density')

'''
# And another image

w, h = 512, 512

with cbook.get_sample_data(P_path) as datafile:
    s = datafile.read()
A = np.frombuffer(s, np.uint16).astype(float).reshape((w, h))
A /= A.max()

fig, ax = plt.subplots()
extent = (0, 25, 0, 25)
im = ax.imshow(A, cmap=plt.cm.hot, origin='upper', extent=extent)

markers = [(15.9, 14.5), (16.8, 15)]
x, y = zip(*markers)
ax.plot(x, y, 'o')

ax.set_title('CT density')

'''
plt.show()