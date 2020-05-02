import pandas as pd

df = pd.DataFrame({'c1': [2, 3]})
df1 = pd.DataFrame({'c2': [5, 6]})
concat = pd.concat([df, df1])
print('{}\n'.format(concat))
