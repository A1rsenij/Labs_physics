import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('2.1.1.xlsx', sheet_name='Лист2')
names = list(data)
N1 = np.array(data[names[0]])
T1 = np.array(data[names[1]])
k1, cov1 = np.polyfit(N1, T1, 1, cov=True)
Tp1 = np.polyval(k1, N1)

N2 = np.array(data[names[2]])
T2 = np.array(data[names[3]])
k2, cov2 = np.polyfit(N2, T2, 1, cov=True)
Tp2 = np.polyval(k2, N2)


fig, ax = plt.subplots(figsize=(10, 6), dpi=100)

ax.scatter(N1, T1, label ='$q = 0,224~г/c$', marker='.')
ax.plot(N1, Tp1, label='$\Delta{T} = $' + '{:.3f}$\pm${:.3f} $\cdot$ N + {:.3f}'.format(k1[0], np.sqrt(cov1[0][0]), k1[1]))
ax.scatter(N2, T2, label ='$q = 0,084~г/c$', marker='.')
ax.plot(N2, Tp2, label='$\Delta{T} = $' + '{:.3f}$\pm${:.3f} $\cdot$ N + {:.3f}'.format(k2[0], np.sqrt(cov2[0][0]), k2[1]))

ax.legend(loc='upper left', fontsize=10)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([0, 1.5, 0, 10])

fig.subplots_adjust(left=0.07)

ax.set_title('Зависимость изменения температуры $\Delta{T}$ от мощности $N$', loc='center', fontsize=15)
ax.set_ylabel('$\Delta{T}, ^{\circ}C$', loc='center', fontsize=10)
ax.set_xlabel('$N, Вт$', loc='center', fontsize=10)

plt.show()

fig.savefig("2.1.1.png", dpi=500)
