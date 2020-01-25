import numpy as np
from mayavi import mlab
from scipy.integrate import odeint
def real(var1, var2, a, b, c):
    x, y, z = var1.tolist()
    return np.array([a*(y-x), x*(b-z)-y, x*y-c*z])
var2 = np.arange(0, 30, 0.01)
add = 1.00
for i in range(10):
	x = odeint(real, (0.0, add, 0.0), var2, args=(10.0, 28.0, 2.6667))
	mlab.plot3d(x[:,0], x[:,1], x[:,2], color=(1, 0.73, 0), tube_radius=0.15)
	add = add + 0.01
mlab.show()

