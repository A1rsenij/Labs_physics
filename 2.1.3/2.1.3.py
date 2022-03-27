import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('2.3.1.xlsx', sheet_name='Лист1')
P1 = np.array(data[list(data)[0]]) * 133.3 * 0.0001
t1 = np.array(data[list(data)[1]])
k1, cov1 = np.polyfit(t1, P1, 1, cov=True)
Pv1 = np.polyval(k1, t1)
data = pd.read_excel('2.3.1.xlsx', sheet_name='Лист2')
P2 = (np.array(data[list(data)[0]]) - 1.4) * 133.3 * 0.0001
t2 = np.array(data[list(data)[1]])
P2 = np.log(P2)
k2, cov2 = np.polyfit(t2, P2, 1, cov=True)
Pv2 = np.polyval(k2, t2)

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.scatter(t2, P2, label ='Улучшение вакуума', marker='.')
ax.plot(t2, Pv2, label='$\ln{P} = $' + '{:.6f}$\pm${:.6f} $\cdot$ t + {:.6f}'.format(k2[0], np.sqrt(cov2[0][0]), k2[1]))

ax.legend(loc='upper right', fontsize=10)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([0, 21, -7, -2])

#fig.subplots_adjust(bottom=0.15, left=0.2)

ax.set_title('Зависимость давления $\ln{P}$ от времени $t$', loc='center', fontsize=15)
ax.set_ylabel('$ln{P} , Па$', loc='center', fontsize=10)
ax.set_xlabel('$t, с$', loc='center', fontsize=10)

plt.show()

fig.savefig("2.3.1_1.png", dpi=500)

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.scatter(t1, P1, label ='Ухудшение вакуума', marker='.')
ax.plot(t1, Pv1, label='$P = $' + '{:.6f}$\pm${:.6f} $\cdot$ t + {:.6f}'.format(k1[0], np.sqrt(cov1[0][0]), k1[1]))

ax.legend(loc='upper left', fontsize=10)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([0, 51, 0, 0.1])

#fig.subplots_adjust(bottom=0.15, left=0.2)

ax.set_title('Зависимость давления $P$ от времени $t$', loc='center', fontsize=15)
ax.set_ylabel('$P , Па$', loc='center', fontsize=10)
ax.set_xlabel('$t, с$', loc='center', fontsize=10)

plt.show()

fig.savefig("2.3.1_2.png", dpi=500)
