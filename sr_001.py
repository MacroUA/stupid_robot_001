import pandas as pd
import matplotlib.pyplot as plt

brothers = 2

delta = 1
hist_look = 2*12*30

part = 3000

df = pd.read_pickle('./data/USDT_BTC_h2.pkl')
#['close' 'date' 'high' 'low' 'open' 'quoteVolume' 'volume' 'weightedAverage']

high = list(df['high'])[-part:]
low = list(df['low'])[-part:]
lo_fo = low


for i in range(hist_look, len(lo_fo)-brothers):
    if lo_fo[i] < lo_fo[i+1]+delta and lo_fo[i] > lo_fo[i+1] - delta:
        plt.plot([0, i], [lo_fo[i], lo_fo[i]], color='gray', alpha = 0.2)

        hist_br = 0
        for o in range(i-hist_look, i):
            if lo_fo[i] < lo_fo[o]+delta and lo_fo[i] > lo_fo[o] - delta:
                hist_br += 1
                print(hist_br)
        if hist_br > 1:
            plt.plot([i-hist_look, i], [lo_fo[i], lo_fo[i]], linewidth=hist_br,  color='green', label = 'power = {}'.format(hist_br))


plt.plot(high, label='High', color='indianred')
plt.plot(low, label='Low', color='royalblue')

plt.legend()
plt.show()

