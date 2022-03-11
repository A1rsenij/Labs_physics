import numpy as np
import matplotlib.pyplot as plt

w = np.array([37.2, 57.1, 87.8, 107.2, 134.3, 171.7, 211.0])
m = np.array([71.7, 109.4, 167.0, 203.5, 251.7, 317.5, 394.0])
k = np.polyfit(m, w, 1)
w1 = np.polyval(k, m)
print(k)

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.plot(m, w1, label='Зависимость', color='orange', linewidth=0.8)

ax.legend(loc='upper left', fontsize=10)

ax.scatter(m, w, color='black', linewidths=0.1,  marker='.')

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([50, 400, 0, 220])

ax.set_title('Зависимость угловой скорости регулярной\n прецесии $\Omega$ от момента силы $M$', loc='center', fontsize=15)
ax.set_ylabel('$\Omega \cdot 10^{-3}$  [рад/c]', loc='center', fontsize=10)
ax.set_xlabel('$M \cdot 10^{-3}$ [H$\cdot$м]', loc='center', fontsize=10)

dk = ((w.mean()/m.mean() - k[0])**2 / 5)**0.5

plt.text(250, 100, 'k = ' + '{:.3f}'.format(k[0]) + '$\pm$' + '{:.3f}'.format(dk), backgroundcolor='white')

plt.show()

fig.savefig("1.2.5.png", dpi=500)
