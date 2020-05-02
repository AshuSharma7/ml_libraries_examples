import numpy as np
arr = np.arange(1, 6)
np.save('arr.npy', arr)
print(repr(np.load('arr.npy')))
