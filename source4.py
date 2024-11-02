# from mpl_toolkits import mplot3d

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
# ax = plt.axes(projection='3d')

xpos = [1, 2, 3, 4, 5]
ypos = [2, 3, 4, 5, 1]
zpos = [0, 0, 0, 0, 0]

dx = np.ones(5)
dy = np.ones(5)
dz = [1, 2, 3, 4, 5]

ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='blue')

plt.show()
