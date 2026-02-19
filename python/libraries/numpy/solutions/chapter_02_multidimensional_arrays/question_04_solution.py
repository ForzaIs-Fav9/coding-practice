import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(arr)
print(arr.reshape(2,8))
print(arr.reshape(8,2))
# Across all three shapes:
# - The total number of elements (16) remains the same.
# - The order of elements in memory remains unchanged.
# What changes:
# - The number of rows and columns.
# - The way the same data is interpreted structurally.
# Reshape does NOT modify data; it only changes how we view it.
