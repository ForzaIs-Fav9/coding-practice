import numpy as np
#Given Python list: [10, 20, 30, 40, 50]
#To convert into a numpy array, we have to use np.array
array = np.array([10, 20, 30, 40, 50])
print(array.dtype)
print(array.shape)
print(array.ndim)
# What these tell us:
# 1) The data type tells us that the data type of this array is integers stored in 64 bits.
# 2) The shape tells us that this is an array with 5 elements in a single row.
# 3) The number of dimensions is 1. This means that this is a 1D array.
