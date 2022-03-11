import numpy as np
import matplotlib.pyplot as plt

### d1 ###
x = np.array([40, 50, 90, 120])
P = np.array([54.9, 62.8, 117.7, 158.9])
k, cov = np.polyfit(x, P, 1, cov=True)
Pa = np.polyval(k, x)

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.scatter(x, P, marker='.', c='orange')
ax.plot(x, Pa, c='orange')

#ax.legend(loc='upper left', fontsize=10)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([30, 130, 50, 160])

#fig.subplots_adjust(bottom=0.15, left=0.2)

ax.set_title('Зависимость перепада давления $\Delta{P}$ от координаты $x$ в трубке $d_1$', loc='center', fontsize=15)
ax.set_ylabel('$\Delta{P}, Па$', loc='center', fontsize=10)
ax.set_xlabel('$x, см$', loc='center', fontsize=10)

plt.show()

fig.savefig("1.3.3_3.png", dpi=500)

### d2 ###
x = np.array([50, 90, 120])
P = np.array([147.1, 264.8, 360.9])
k, cov = np.polyfit(x, P, 1, cov=True)
Pa = np.polyval(k, x)

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.scatter(x, P, marker='.', c='orange')
ax.plot(x, Pa, c='orange')

#ax.legend(loc='upper left', fontsize=10)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([40, 130, 140, 370])

#fig.subplots_adjust(bottom=0.15, left=0.2)

ax.set_title('Зависимость перепада давления $\Delta{P}$ от координаты $x$ в трубке $d_2$', loc='center', fontsize=15)
ax.set_ylabel('$\Delta{P}, Па$', loc='center', fontsize=10)
ax.set_xlabel('$x, см$', loc='center', fontsize=10)

plt.show()

fig.savefig("1.3.3_4.png", dpi=500)
