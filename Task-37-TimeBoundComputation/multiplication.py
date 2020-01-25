import random
from random import seed
from random import randint
import time
import numpy as np 


num_rows = 10
num_columns = 10
seed(1)
random_matrix = [[random.randint(0,10) for j in range(num_rows)] for i in range(num_columns)]
seed(1)
random_matrix1 = [[random.randint(0,10) for j in range(num_rows)] for i in range(num_columns)]
res = [[0 for x in range(num_rows)] for y in range(num_columns)] 

start_time = time.time()
for i in range(len(random_matrix)): 
    for j in range(len(random_matrix1[0])): 
        for k in range(len(random_matrix1)): 
            res[i][j] += random_matrix[i][k] * random_matrix1[k][j] 
print (res)
print("%s seconds" % (time.time() - start_time))


start_time = time.time()
res = np.dot(random_matrix, random_matrix1)
print(res)
print("%s seconds" % (time.time() - start_time))

