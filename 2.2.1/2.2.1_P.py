import numpy as np
import matplotlib.pyplot as plt

P = np.array([40, 77.5, 120, 154, 206, 236])
D = np.array([9.81, 5.03, 4.08, 2.91, 2.39, 1.98])
P = 1/P

k, cov = np.polyfit(P, D, 1, cov=True)
Dk = np.polyval(k, P)

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.scatter(P, D, marker='.', c='blue')
ax.plot(P, Dk, label='$D = $' + '{:.3f}$\pm${:.3f}'.format(k[0], np.sqrt(cov[0][0])) + '$\cdot P^{-1}$ + ' +'{:.3f}'.format(k[1]), c='orange')

ax.legend(loc='upper left', fontsize=10)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([0, 0.03, 1, 11])

#fig.subplots_adjust(bottom=0.15, left=0.2)

ax.set_title('Зависимость $D(1/P)$', loc='center', fontsize=15)
ax.set_ylabel('$D , см^2/c$', loc='center', fontsize=10)
ax.set_xlabel('$1/P, торр^{-1}$', loc='center', fontsize=10)

plt.show()

fig.savefig("2.2.1_2.png", dpi=500)
