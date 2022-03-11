import numpy as np
import matplotlib.pyplot as plt

def dk(T, P, k):
    n = len(T)
    x = (T**2).mean()
    y = (P**2).mean()
    d = n ** (-0.5) * (abs(y/x - k[0]*2)) ** 0.5
    return d

Pnagr = np.array([2639.34, 2745.98, 2985.92, 3172.54, 3332.5, 3545.78, 3652.42, 3812.38, 4132.3, 4398.9, 4582.52, 4772.14, 5038.74, 5465.3, 5625.26, 6078.48, 6371.74, 6665, 6904.94])
Post = np.array([2612.68, 2799.3, 2905.94, 3172.54, 3359.16, 3652.42, 3865.7, 4078.98, 4238.94, 4398.9, 4665.6, 4878.78, 5252.02, 5491.96, 5731.9, 6051.82, 6291.76, 6744.98, 6904.94])
T = np.array([22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])
T += 273
knagr = np.polyfit(T, Pnagr, 1)
kost = np.polyfit(T, Post, 1)
Pn = np.polyval(knagr, T)
Po = np.polyval(kost, T)

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.scatter(T, Pnagr, marker='.', c='orange', label='Нагрев')
ax.plot(T, Pn, c='orange', label='P = ({:.3f}$\pm${:.3f}) * T + ({:.3f})'.format(knagr[0], dk(T, Pnagr, knagr), knagr[1]))
ax.scatter(T, Post, marker='.', c='blue', label='Охлаждение')
ax.plot(T, Po, c='blue', label='P = ({:.3f}$\pm${:.3f}) * T + ({:.3f})'.format(kost[0], dk(T, Post, kost), kost[1]))


ax.legend(loc='upper left', fontsize=10)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([293, 315, 2000, 7000])

#fig.subplots_adjust(bottom=0.15, left=0.2)

ax.set_title('Зависимость давления паров P от температуры T', loc='center', fontsize=15)
ax.set_ylabel('$P, Па$', loc='center', fontsize=10)
ax.set_xlabel('$T, ^{\circ}K$', loc='center', fontsize=10)

plt.show()

fig.savefig("2.4.1_1.png", dpi=500)

T = 1/T
Pnagr = np.log(Pnagr)
Post = np.log(Post)
knagr = np.polyfit(T, Pnagr, 1)
kost = np.polyfit(T, Post, 1)
Pn = np.polyval(knagr, T)
Po = np.polyval(kost, T)

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.scatter(T, Pnagr, marker='.', c='orange', label='Нагрев')
ax.plot(T, Pn, c='orange', label='$\ln{P}$' + ' = ({:.3f}$\pm${:.3f}) * '.format(knagr[0], dk(T, Pnagr, knagr)) + '$T^{-1}$' + ' + ({:.3f})'.format(knagr[1]))
ax.scatter(T, Post, marker='.', c='blue', label='Охлаждение')
ax.plot(T, Po, c='blue', label='$\ln{P}$' + ' = ({:.3f}$\pm${:.3f}) * '.format(kost[0], dk(T, Post, kost)) + '$T^{-1}$' + ' + ({:.3f})'.format(kost[1]))


ax.legend(loc='upper right', fontsize=10)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([0.003175, 0.0034, 7.8, 8.9])

#fig.subplots_adjust(bottom=0.15, left=0.2)

ax.set_title('Зависимость в координатах $1/T, \ln{P}$', loc='center', fontsize=15)
ax.set_ylabel('$\ln{P}$', loc='center', fontsize=10)
ax.set_xlabel('$1/T, ^{\circ}K^{-1}$', loc='center', fontsize=10)

plt.show()

fig.savefig("2.4.1_2.png", dpi=500)
