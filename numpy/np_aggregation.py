import numpy as np


# Sum of an Array using np.sum
arr = ([[4, 6, 34], [-8, 0, 4], [-7, -8, 4]])
print(np.sum(arr))
print(np.sum(arr, axis=0))

# Cumulative Sum using np.cumsum
print(np.cumsum(arr))
print(np.cumsum(arr, axis=0))

# Array Concatenation using np.concatenate
arr1 = np.array([[5, 567, 34], [6, 7, 4], [89, 6, 45]])
print(repr(np.concatenate([arr, arr1])))
