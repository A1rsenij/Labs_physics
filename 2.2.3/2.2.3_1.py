import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('2.2.3.xlsx', sheet_name='Лист2')
names = list(data)

T = np.array([23.1, 35, 45, 70])
colors = np.array(['blue', 'green', 'purple', 'red'])

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)

for i in range(0, 16, 4):
    Q = np.array(data[names[i]])
    index = Q.argmin()
    Q = np.delete(Q, index)
    dQ = np.delete(np.array(data[names[i + 1]]), index)
    R = np.delete(np.array(data[names[i + 2]]), index)
    dR = np.delete(np.array(data[names[i + 3]]), index)
    k, cov = np.polyfit(Q, R, 1, cov=True)
    Rp = np.polyval(k, Q)
    plotline, caps, barlinecols = ax.errorbar(Q, R, xerr=dQ, yerr=dR, marker='.', label='$T = $' + str(T[i // 4]) + '$~^{\circ}C$', linestyle='none', color=colors[i // 4], capsize=5)
    ax.plot(Q, Rp, label='$R = $' + '{:.3f}$\pm${:.3f} $\cdot$ Q + {:.3f}$\pm${:.3f}'.format(k[0], np.sqrt(cov[0][0]), k[1], np.sqrt(cov[1][1])), color=colors[i // 4])

ax.legend(loc='upper left', fontsize=10)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([0, 0.15, 9, 20])

fig.subplots_adjust(left=0.07)

ax.set_title('Зависимость сопротивления проволоки $R$ от мощности $Q$', loc='center', fontsize=15)
ax.set_ylabel('$R, Ом$', loc='center', fontsize=10)
ax.set_xlabel('$Q, Дж$', loc='center', fontsize=10)

plt.show()

fig.savefig("2.2.3_1.png", dpi=500)
