import pandas as pd

csv_file = './data/eurousd_1h_csv.csv'
df = pd.read_csv(csv_file, delimiter=';')
print(df.columns.values)
print(df.head(5))
df.to_pickle(csv_file[:-3]+'pkl')