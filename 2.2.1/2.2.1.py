import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

names = ['40', '80', '120', '160', '200', '240']

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
for i in names:
    data = pd.read_csv(i + '.csv', delimiter=',')
    t = np.array(data[list(data)[0]])
    u = np.array(data[list(data)[1]])
    u = np.log(u)
    k, cov = np.polyfit(t, u, 1, cov=True)
    uv = np.polyval(k, t)
    ax.scatter(t, u, label ='P = ' + i + ' торр', marker='.')
    ax.plot(t, uv, label='$\ln(U) = $' + '{:.6f}$\pm${:.6f} $\cdot$ t + {:.6f}'.format(k[0], np.sqrt(cov[0][0]), k[1]))

ax.legend(loc='upper right', fontsize=10)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([0, 420, 2, 4])

#fig.subplots_adjust(bottom=0.15, left=0.2)

ax.set_title('Зависимость напряжения $U$ от времени $t$', loc='center', fontsize=15)
ax.set_ylabel('$ln(U) , мВ$', loc='center', fontsize=10)
ax.set_xlabel('$t, с$', loc='center', fontsize=10)

plt.show()

fig.savefig("2.2.1_1.png", dpi=500)
