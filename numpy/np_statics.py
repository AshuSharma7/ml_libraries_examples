import numpy as np

# Obtaining least and greatest no. in numoy array
arr = np.array([[2, 6, -9], [-8, 54, 7], [0, -4, 67]])
print(arr.max())
print(arr.min())
print(repr(arr.max(axis=1)))
print(repr(arr.max(axis=0)))
print(repr(arr.min(axis=-1)))

# Mean, Median, Variance
print(np.mean(arr))
print(np.median(arr))
print(np.var(arr))
