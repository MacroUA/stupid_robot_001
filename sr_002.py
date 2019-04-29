import pandas as pd
import matplotlib.pyplot as plt

brothers = 2
delta = .00003
hist_look = 100

part = 100

df = pd.read_csv('./data/eurousd_1h_csv.csv', delimiter=';', encoding='utf-8')
print(df.columns.values) #['Date' 'Open' 'High' 'Low' 'Close']

for i in range(len(df['Low'])):
    try:
        print(float(df['Low'][i]))
    except Exception:
        print(df['Date'][i])
        input('error')

exit()

part = len(df) #закоментувати якщо потрібна частина данних

high = list(df['High'])[-part:]
low = list(df['Low'])[-part:]

#high = [float(el) for el in high if type(el) is str]
#low = [float(el) for el in low if type(el) is str]

lo_fo = low
print(lo_fo)
exit()


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
