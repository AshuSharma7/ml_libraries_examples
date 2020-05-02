import pandas as pd

# Pandas Series function to create Series
sr = pd.Series([[2, 3], [4, 5]], ['a', 'b'])
print(repr(sr))

# Using index with pandas Series
sr = pd.Series([2, 4, 7, 4], index=['a', 'b', 'c', 'd'])
print(repr(sr))

# Dictionary input in Pandas Series
sr = pd.Series({'a': 2, 'b': 3, 'd': 1, 'e': 4})
print(repr(sr))
sr = pd.Series([[2, 5, 57], [53, 56, 0]])
print(repr(sr))
