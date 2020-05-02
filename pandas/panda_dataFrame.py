import pandas as pd
df = pd.DataFrame([[2, 3.0], [5, 7.8]], index=[
                  'r1', 'r2'], columns=['c1', 'c2'])
print('{}\n'.format(df))
print(df.dtypes)
sr = pd.DataFrame([[2, 4, 5], [5, 9, -4], [0, -20, 5]], index=['r1', 'r2', 'r3'],
                  columns=['c1', 'c2', 'c3'])
print(repr(sr))

sr = pd.Series({'c1': [2, 5, -5], 'c2': [4, 67, 50],
                'c3': [-4, -67, 0], }, index=['r1', 'r2', 'r3'])
print(repr(sr))
