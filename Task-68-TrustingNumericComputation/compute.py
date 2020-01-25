from numpy.linalg import inv
import numpy as np
from numpy import linalg as LA

#Matrix 1
a = [[ 1.,  -0.098, -0.008, -0.849],
 [-0.098,  1.,    -0.382, -0.25 ],
 [-0.008, -0.382,  1.,    -0.239],
 [-0.849, -0.25,  -0.239,  1.   ]]
print("\n")
print("Matrix 1 condition number: ", LA.cond(a))
print("Its inverse condition number: ", LA.cond(inv(a)))
print(np.dot(a,inv(a)))
print("\n")
b = [[ 1.,     0.996, -0.845,  0.333],
 [ 0.996,  1.,    -0.891,  0.378],
 [-0.845, -0.891 , 1. ,   -0.282],
 [ 0.333,  0.378 ,-0.282 , 1.   ]]
print("Matrix 2 condition number: ",LA.cond(b))
print("Its inverse condition number: ",LA.cond(inv(b)))
x = np.dot(b, inv(b))
print(np.dot(b,inv(b)))
print("\n")

c = [[ 1.,     0.656,  0.737, -0.527],
 [ 0.656,  1.,     0.59,  -0.305],
 [ 0.737,  0.59,   1.,    -0.94 ],
 [-0.527, -0.305, -0.94,   1.   ]]
print("Matrix 3 condition number: ",LA.cond(c))
print("Its inverse condition number: ",LA.cond(inv(c)))
x = np.dot(c, inv(c))
print(np.dot(c,inv(c)))
print("\n")

d = [[ 1.,    -0.627, -0.629,  0.905],
 [-0.627,  1.,    -0.459, -0.173],
 [-0.629, -0.459,  1.,    -0.916],
 [ 0.905, -0.173, -0.916,  1.   ]]
print("Matrix 4 condition number: ",LA.cond(d))
print("Its inverse condition number: ",LA.cond(inv(d)))
x = np.dot(d, inv(d))
print(np.dot(d,inv(d)))
print("\n")

e = [[ 1.,   -0.26, -0.515,  0.257],
 [-0.26,   1.,    -0.653, -0.483],
 [-0.515, -0.653,  1.,    -0.009],
 [ 0.257, -0.483, -0.009,  1.   ]]
print("Matrix 5 condition number: ",LA.cond(e))
print("Its inverse condition number: ",LA.cond(inv(e)))
x = np.dot(e, inv(e))
print(np.dot(e,inv(e)))
print("\n")

f = [[ 1.,     0.416, -0.418,  0.022],
 [ 0.416,  1.,    -0.749, -0.586],
 [-0.418, -0.749,  1.,    -0.086],
 [ 0.022, -0.586, -0.086,  1.   ]]
print("Matrix 5 condition number: ",LA.cond(f))
print("Its inverse condition number: ",LA.cond(inv(f)))
x = np.dot(f, inv(f))
print(np.dot(f,inv(f)))
print("\n")

