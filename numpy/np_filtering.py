import numpy as np
# Numpy has direct filtering by applying operations on arraty dierctly
arr = np.array([[3, 6, -8], [0, -2, 4], [10, 5, 23]])
print(repr(arr % 2 == 0))
print(repr(~(arr > 0)))

# Filtering np.nan
arr_nan = np.array([np.nan, 2, 4])
print(repr(np.isnan(arr_nan)))

# Filtering using np.where

arr_where = np.array([[3, 5, -9], [5, 0, 20], [5, -45, 0]])
row, column = np.where(arr_where == 5)
print(repr(row))
print(repr(column))

# Filtering Using np.any & np.all

np.any(arr > 5)
print(repr(np.all(arr > 0)))
print(repr(np.any(arr > 0, axis=0)))

# FIltering Using np.where with 3 arguments

zeros = np.zeros_like(arr_where)
where_zeros = np.where(arr_where > 0, arr_where, zeros)
print(repr(where_zeros))

coin_flips = np.random.randint(2, size=(2, 3))
print(repr(coin_flips))
bool_coin_flips = coin_flips.astype(dtype=np.bool)
print(repr(bool_coin_flips))
