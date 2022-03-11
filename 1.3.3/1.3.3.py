import numpy as np
import matplotlib.pyplot as plt

### d1 ###
Plam = np.array([49.03, 62.76, 74.53, 84.33, 98.07, 109.83, 115.72])
Ptur = np.array([176.52, 213.78, 256.93, 278.51, 319.7, 351.08, 380.5])
Qlam = np.array([4.32, 6.74, 7.81, 8.93, 10.39, 11.44, 11.92])
Qtur = np.array([13.85, 14.7, 15.89, 16.57, 17.71, 18.33, 19.37])
klam, covlam = np.polyfit(Plam, Qlam, 1, cov=True)
Qlm = np.polyval(klam, Plam)

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.scatter(Plam, Qlam, marker='.', c='orange', label='Ламинарное течение')
ax.plot(Plam, Qlm, c='orange', label='$Q \cdot 10^{-5}$' + ' = ({:.3f}$\pm${:.3f})$\cdot \Delta P$ + ({:.3f})'.format(klam[0], np.sqrt(covlam[0][0]), klam[1]))
ax.scatter(Ptur, Qtur, marker='.', c='blue', label='Турбулентное течение')

ax.legend(loc='upper left', fontsize=10)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([30, 360, 3, 20])

#fig.subplots_adjust(bottom=0.15, left=0.2)

ax.set_title('Зависимость расхода $Q$ от перепада давления $\Delta{P}$ в трубке $d_1$', loc='center', fontsize=15)
ax.set_ylabel('$Q \cdot 10^{-5}, м^3/c$', loc='center', fontsize=10)
ax.set_xlabel('$\Delta{P}, Па$', loc='center', fontsize=10)

plt.show()

fig.savefig("1.3.3_1.png", dpi=500)

### d2 ###
Plam = np.array([82.38, 58.84, 41.19, 100.03, 121.6, 109.84, 129.45])
Ptur = np.array([156.91, 237.32, 282.43, 349.12, 404.03, 162.79, 198.09])
Qlam = np.array([5.36, 3.56, 2.58, 5.86, 7.04, 6.49, 7.6])
Qtur = np.array([8.8, 10.29, 11.13, 12.19, 13.04, 8.87, 9.55])
klam, covlam = np.polyfit(Plam, Qlam, 1, cov=True)
Qlm = np.polyval(klam, Plam)

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.scatter(Plam, Qlam, marker='.', c='orange', label='Ламинарное течение')
ax.plot(Plam, Qlm, c='orange', label='$Q \cdot 10^{-5}$' + ' = ({:.3f}$\pm${:.3f})$\cdot \Delta P$ + ({:.3f})'.format(klam[0], np.sqrt(covlam[0][0]), klam[1]))
ax.scatter(Ptur, Qtur, marker='.', c='blue', label='Турбулентное течение')

ax.legend(loc='upper left', fontsize=10)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([30, 420, 2, 14])

#fig.subplots_adjust(bottom=0.15, left=0.2)

ax.set_title('Зависимость расхода $Q$ от перепада давления $\Delta{P}$ в трубке $d_2$', loc='center', fontsize=15)
ax.set_ylabel('$Q \cdot 10^{-5}, м^3/c$', loc='center', fontsize=10)
ax.set_xlabel('$\Delta{P}, Па$', loc='center', fontsize=10)

plt.show()

fig.savefig("1.3.3_2.png", dpi=500)
