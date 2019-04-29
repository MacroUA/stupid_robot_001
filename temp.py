import pandas as pd
a = {'laters':['a','b','c']}

df = pd.DataFrame(a)

print(df.iloc[::-1].reset_index(drop=True))
