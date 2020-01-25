import random
from random import seed
from random import randint
import time
import numpy as np 
from functools import partial
from matplotlib import pyplot as plt 
import timeit

def order(random_matrix, random_matrix1):
	res = [[0 for x in range(num_rows)] for y in range(num_columns)] 
	for i in range(len(random_matrix)): 
		for j in range(len(random_matrix1[0])): 
			for k in range(len(random_matrix1)): 
				res[i][j] += random_matrix[i][k] * random_matrix1[k][j]
	return res
#def disorder(random_matrix, random_matrix1):
#	res = [[0 for x in range(num_rows)] for y in range(num_columns)] 
#	for i in range(len(random_matrix)): 
#		for k in range(len(random_matrix1[0])): 
#			for j in range(len(random_matrix1)): 
#				res[i][j] += random_matrix[i][k] * random_matrix1[k][j]
#	return res

if __name__ == '__main__':
	t1 =[]
#	t2 =[]
	rng = range(1,1000,100)
	for n in rng:
		num_rows = n
		num_columns = n
		random.seed(1)
		random_matrix = [[random.randint(0,10) for j in range(num_rows)] for i in range(num_columns)]
		random.seed(2)
		random_matrix1 = [[random.randint(0,10) for j in range(num_rows)] for i in range(num_columns)]
		start1 = timeit.default_timer()
		func1 = order(random_matrix,random_matrix1)
		#print(np.ravel(func1))
		stop1 = timeit.default_timer()
	#	start2 = timeit.default_timer()
	#	func2 = disorder(random_matrix,random_matrix1)
		#print(np.ravel(func2))
	#	stop2 = timeit.default_timer()
		t1.append(stop1 - start1)
	#	t2.append(stop2 - start2)
	plt.plot(rng,t1)
	#plt.plot(rng,t2)
	plt.ylabel('Execution time')
	plt.xlabel('Problem size')
	#plt.legend()
	plt.show()