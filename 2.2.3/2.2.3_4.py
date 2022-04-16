import numpy as np
import matplotlib.pyplot as plt

T = np.array([23.1, 35, 45, 70])
T += 273
T = np.log(T)
kap = np.array([0.029, 0.031, 0.026, 0.049])
kap = np.log(kap)
k, cov = np.polyfit(T, kap, 1, cov=True)
kp = np.polyval(k, T)

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.scatter(T, kap, marker='.')
ax.plot(T, kp, label="$ln(\kappa) = $" + '{:.3f}$\pm${:.3f} $\cdot$ ln(T) + {:.3f}'.format(k[0], np.sqrt(cov[0][0]), k[1]))

ax.legend(loc='upper left', fontsize=10)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([0.9 * np.log(20 + 273), 1.1 * np.log(75 + 273), 0.9 * np.log(0.049), 1.1 * np.log(0.026)])

fig.subplots_adjust(left=0.07)

ax.set_title('Зависимость $ln(\kappa)$ от $ln(T)$', loc='center', fontsize=15)
ax.set_ylabel('$ln(\kappa)$', loc='center', fontsize=10)
ax.set_xlabel('$ln(T)$', loc='center', fontsize=10)

plt.show()

fig.savefig("2.2.3_4.png", dpi=500)
