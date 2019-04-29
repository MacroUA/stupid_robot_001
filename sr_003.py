import pandas as pd
import matplotlib.pyplot as plt
from config.config_000 import *

df = pd.read_csv(file , delimiter='	', encoding='utf-8')
print(df.columns.values) #['Date' 'Open' 'High' 'Low' 'Close']

if reverse:
    df = df.iloc[::-1].reset_index(drop=True)

if not part:
    part = len(df) #cut data

data = list(df[target])[-part:]


for i in range(len(data)-2, hist_look, -1):
    if data[i] < data[i-1]+delta and data[i] > data[i-1] - delta:
        plt.plot([i-hist_look, i], [data[i], data[i]], color='gray', alpha = 0.2)

        hist_br = 0
        for o in range(i-hist_look, i):
            if data[i] < data[o]+delta and data[i] > data[o] - delta:
                hist_br += 1
                plt.scatter(o, data[o], s=20, c='green', alpha=1, linewidths=None)
                print(hist_br)
        if hist_br > 1:
            plt.plot([i-hist_look, i], [data[i], data[i]], linewidth=hist_br,  color='green', label = 'power = {}'.format(hist_br))



plt.plot(df['High'], label ='High', color ='indianred', alpha=0.5, linewidth=5)
plt.plot(df['Low'], label ='Low', color ='royalblue', alpha=0.5, linewidth=5)
plt.plot(data, label=target, color='blue', linewidth=1)

plt.legend()
plt.show()
