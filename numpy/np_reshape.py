import numpy as np
# numpy arange fumction similar to range available in the python
arr = np.arange(10)
# numpy reshape function
reshape_arr = np.reshape(arr, (2, 5))
print(repr(arr))
print("arr shape: {}".format(arr))
print(repr(reshape_arr))
print("reshape_arr : {}".format(reshape_arr.shape))
areshape = np.reshape(reshape_arr, (5, 2))
print(repr(areshape))
# Numpy Flatten Function
flatten = areshape.flatten()
print(repr(flatten))

# numpy transpose function row to columns and columns to rows
tran = np.transpose(reshape_arr)
print(repr(tran))

tran = np.transpose(reshape_arr, axes=[0, 1])
print("New Shape: {}".format(tran.shape))

linspaced_arr = np.linspace(1.9, 50.1, num=100)
print(repr(linspaced_arr))
print("Linespace array: {}".format(linspaced_arr.size))
line_reshape = np.reshape(linspaced_arr, (5, 4, 5))
