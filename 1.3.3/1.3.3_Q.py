import numpy as np
import matplotlib.pyplot as plt

### d1 ###
r = np.array([5.25/2, 3.9/2])
r = np.log(r)
qlam = np.array([11.95, 4.07])
qlam = np.log(qlam)
klam= np.polyfit(r, qlam, 1)
ql = np.polyval(klam, r)
qtur = np.array([23.22, 11.08])
qtur = np.log(qtur)
ktur = np.polyfit(r, qtur, 1)
qt = np.polyval(ktur, r)
#1
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6), dpi=100)
plt.subplot(1, 2, 1)
ax1.scatter(r, qlam, marker='.', c='orange', label='$\Delta{P} / l = 2/3~[дел/см]$')
ax1.plot(r, ql, c='orange', label='a = {:.3f}'.format(klam[0]))

ax1.legend(loc='upper left', fontsize=10)

ax1.grid(which="major", linewidth=0.5)
ax1.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax1.axis([0.5, 1.1, 1.2, 2.8])

#fig.subplots_adjust(bottom=0.15, left=0.2)

ax1.set_title('Ламинарное течение', loc='center', fontsize=10)
ax1.set_ylabel('$\ln{Q}$', loc='center', fontsize=10)
ax1.set_xlabel('$\ln{R}$', loc='center', fontsize=10)
#2
plt.subplot(1, 2, 2)

ax2.scatter(r, qtur, marker='.', c='orange', label='$\Delta{P} / l = 3~[дел/см]$')
ax2.plot(r, qt, c='orange', label='a = {:.3f}'.format(ktur[0]))

ax2.legend(loc='upper left', fontsize=10)

ax2.grid(which="major", linewidth=0.5)
ax2.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax2.axis([0.5, 1.1, 2, 3.4])

ax2.set_title('Турбулентное течение', loc='center', fontsize=10)
ax2.set_ylabel('$\ln{Q}$', loc='center', fontsize=10)
ax2.set_xlabel('$\ln{R}$', loc='center', fontsize=10)

fig.suptitle('Зависимость расхода $\ln{Q}$ от радиуса трубки $\ln{R}$ при постоянном градиенте $\Delta{P}/l$')

plt.show()

fig.savefig("1.3.3_5.png", dpi=500)
