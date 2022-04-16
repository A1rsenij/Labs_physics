import numpy as np
import matplotlib.pyplot as plt

T = np.array([23.1, 35, 45, 70])
R = np.array([10.981, 11.083, 11.484, 12.713])
k, cov = np.polyfit(T, R, 1, cov=True)
Rp = np.polyval(k, T)

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.scatter(T, R, marker='.')
ax.plot(T, Rp, label="$R = $" + '{:.3f}$\pm${:.3f} $\cdot$ T + {:.3f}'.format(k[0], np.sqrt(cov[0][0]), k[1]))

ax.legend(loc='upper left', fontsize=10)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([20, 75, 10, 14])

fig.subplots_adjust(left=0.07)

ax.set_title('Зависимость сопротивления проволоки $R_0$ от температуры $T$', loc='center', fontsize=15)
ax.set_ylabel('$R_0, Ом$', loc='center', fontsize=10)
ax.set_xlabel('$T, ^{\circ}C$', loc='center', fontsize=10)

plt.show()

fig.savefig("2.2.3_2.png", dpi=500)
