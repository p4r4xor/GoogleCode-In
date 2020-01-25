# Numpy vs ordinary multiplication

The reason why Numpy is faster is most of it is written in C. And O(n^3) multiplication algorithm is always slower in python when compared to C if no modules are involved. 

Matrix Multiplications in Numpy are mostly parallel computed, and Numpy arrays are specialized data structures which in real life are most valuable. From the following task, we see that at the instance n = 1000 as our matrix, normal O(n^3) took around 80 seconds and Numpy's np.dot() took around 2 seconds. 

![linear](https://user-images.githubusercontent.com/59208177/71449551-b952cb80-271c-11ea-8277-732049540e72.png)


