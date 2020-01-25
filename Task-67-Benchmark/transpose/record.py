import random
from random import seed
from random import randint
import time
import numpy as np 
from functools import partial
from matplotlib import pyplot as plt 
import timeit

cpp = [1.474320, 1.773271, 5.730233, 2.654410, 4.829852, 4.499110]
python = [7.780963557990617, 9.574131483008387, 11.152830653998535, 13.10648023999238, 14.799838357997942, 16.78674758799025]
julia = [0.005498, 0.005565, 0.005616, 0.005610, 0.005633, 0.005735]
rng = [10000,11000,12000,13000,14000,15000]
plt.plot(rng,cpp, label='C++')
plt.plot(rng,python, label='Python')
plt.plot(rng,julia, label='Julia')
plt.ylabel('Execution time')
plt.xlabel('Matrix size')
plt.legend()
plt.show()