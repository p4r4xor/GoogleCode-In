import random
from random import seed
from random import randint
import time
import numpy as np 
from functools import partial
from matplotlib import pyplot as plt 
import timeit

cpp = [39.606926, 55.108298, 71.952373, 88.254272, 110.807373, 143.531006]
python = [55.79228675000195, 69.06534739599738, 95.44301002999418, 116.55834482099453, 148.10256004201074, 181.89852783699462]
julia = [60.672020, 80.054933, 102.255384, 132.648907, 162.305175, 199.261677]
rng = [10000,11000,12000,13000,14000,15000]
plt.plot(rng,cpp, label='C++')
plt.plot(rng,python, label='Python')
plt.plot(rng,julia, label='Julia')
plt.ylabel('Execution time')
plt.xlabel('Matrix size')
plt.legend()
plt.show()