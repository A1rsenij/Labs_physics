import numpy as np
import matplotlib.pyplot as plt

T = np.array([23.1, 35, 45, 70])
kap = np.array([0.029, 0.031, 0.026, 0.049])
k, cov = np.polyfit(T, kap, 1, cov=True)
kp = np.polyval(k, T)

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.scatter(T, kap, marker='.')
ax.plot(T, kp, label="$\kappa = $" + '{:.6f}$\pm${:.6f} $\cdot$ T + {:.6f}'.format(k[0], np.sqrt(cov[0][0]), k[1]))

ax.legend(loc='upper left', fontsize=10)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([20, 75, 0, 0.055])

fig.subplots_adjust(left=0.07)

ax.set_title('Зависимость коэффициента теплопроводности $\kappa$ от температуры $T$', loc='center', fontsize=15)
ax.set_ylabel('$\kappa, Вт/(K \cdot м)$', loc='center', fontsize=10)
ax.set_xlabel('$T, ^{\circ}C$', loc='center', fontsize=10)

plt.show()

fig.savefig("2.2.3_3.png", dpi=500)
