import numpy as np
# array slicing
arr = np.array([[2, 3, 6], [5, 8, 10], [23, 8, 9]])
print(repr(arr[1:, 2:]))
# Array Argmax, argmin
print(np.argmax(arr[0]))
print(np.argmin(arr, axis=1))
