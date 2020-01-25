# Space Bound Computation

This task is based on checking/verifying the time taken for the matrix multiplication which performs in the order O(n<sup>3</sup>) time complexity. In this particular task, we change the order of looping and check if the time complexity changes or not.

To see what changed, I've attached the following.
![order](https://user-images.githubusercontent.com/59013403/71606765-d97df280-2b41-11ea-9a15-1083fa2a349e.png)
![disorder](https://user-images.githubusercontent.com/59013403/71606768-dd117980-2b41-11ea-825d-26171e16681f.png)

Normally, there wouldn't be much difference between both of them running at smaller values of n. But at larger values, we can notice the change as it gets decreased by a lot. 

The main reason for how the things work is due to the cache accumulation during one process over the other. This happens during accessing arrays in a different manner. We would see a significant change if we ran the same in C/C++, but due to python code is virtually compiled to bytecode and a lot of compiler optimization occurs.

### Terms to be familiarized
 

**Caching**: Caching is the practice of storing data in and retrieving data from a high-performance store (usually memory) either explicitly or implicitly.

**Cache Miss**: A cache miss is when something is looked up in the cache and is not found – the cache did not contain the item being looked up.

**Row-major order vs Column-major order**

![row](https://user-images.githubusercontent.com/59013403/71608242-ca04a680-2b4d-11ea-8e59-79971e9d51f1.png)

![fort](https://user-images.githubusercontent.com/59013403/71608488-ab9faa80-2b4f-11ea-9c56-2bb51015b5d0.png)

**Numpy's ravel**: `numpy.ravel(a, order='C')` where `C` can be replaced with any one of `{C,F,A,K}`. The letter represents the language used (`C` for `C` in `row-major ordering` and `F` for `Fortran` in `column-major ordering`.

For example:
```python
>>> x = np.array([[1, 2, 3], [4, 5, 6]])
>>> np.ravel(x, order='C')
array([1, 2, 3, 4, 5, 6])
>>> np.ravel(x, order='F')
array([1, 4, 2, 5, 3, 6])
```
Let us now look at individual codes and analyze the following.
### First 
```python
def order(random_matrix, random_matrix1):
	res = [[0 for x in range(num_rows)] for y in range(num_columns)] 
	for i in range(len(random_matrix)): 
		for j in range(len(random_matrix1[0])): 
			for k in range(len(random_matrix1)): 
				res[i][j] += random_matrix[i][k] * random_matrix1[k][j]
```

As we see at the lower-level loop, k is increasing linearly and this means that when running the inner-most loop, every iteration is likely to have a cache miss during accessing the value `random_matrix1[k][j]`. The reason for this is that because the matrix is stored in row-major order, each time you increment k, you're skipping over an entire row of the matrix and jumping much further into memory, possibly far past the values you've cached. However, you don't have a miss when looking up `res[i][j]` (since i and j are the same), nor will you probably miss `random_matrix[i][k]`, because the values are in row-major order and if the value of `random_matrix[i][k]` is cached from the previous iteration, the value of `random_matrix[i][k]` read on this iteration is from an adjacent memory location. Consequently, on each iteration of the innermost loop, you are likely to have one cache miss.
### Second
```python
def disorder(random_matrix, random_matrix1):
	res = [[0 for x in range(num_rows)] for y in range(num_columns)] 
	for i in range(len(random_matrix)): 
		for k in range(len(random_matrix1[0])): 
			for j in range(len(random_matrix1)): 
				res[i][j] += random_matrix[i][k] * random_matrix1[k][j]
	return res
```
Since the values are in row-major order, the value of `res[i][j]` is likely to be in-cache, because the value of `res[i][j]` from the previous iteration is likely cached as well and ready to be read. Similarly, `random_matrix1[k][j]` is probably cached, and since i and k aren't changing, chances are `random_matrix[i][k]` is cached as well. This means that on each iteration of the inner loop, you're likely to have no cache misses.

### Final Image for comparision
The upper limit was `n=900`. At `n=1000`, the compute time is 2 minutes alone which means at `n=2000` will take around 16 minutes (we see some real difference at this level)

![spacebound](https://user-images.githubusercontent.com/59013403/71610592-4dc78e80-2b60-11ea-89ea-8d132c75e48e.png)


### Resources
[1] https://stackoverflow.com/questions/7395556/why-does-the-order-of-loops-in-a-matrix-multiply-algorithm-affect-performance

[2] https://en.wikipedia.org/wiki/Locality_of_reference#Use_of_spatial_and_temporal_locality:_hierarchical_memory

[3]  https://en.wikipedia.org/wiki/Loop_interchange#The_utility_of_loop_interchange

[4] https://stackoverflow.com/questions/9936132/why-does-the-order-of-the-loops-affect-performance-when-iterating-over-a-2d-arra

[5] https://stackoverflow.com/questions/35631216/matrix-multiplication-kij-order-parallel-version-slower-than-non-parallel
