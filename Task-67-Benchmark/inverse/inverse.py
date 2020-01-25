from numpy.linalg import inv
import random
from random import seed
from random import randint
import time
import numpy as np 
from functools import partial
from matplotlib import pyplot as plt 
import timeit

num_rows = 15000
num_columns = 15000

random_matrix = [[random.randint(0,1) for j in range(num_rows)] for i in range(num_columns)]
start2 = timeit.default_timer()
ainv = inv(np.matrix(random_matrix))
stop2 = timeit.default_timer()
#print(random_matrix)
#print(ainv)
print(stop2 - start2)