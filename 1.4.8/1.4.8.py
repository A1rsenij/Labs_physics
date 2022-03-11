import numpy as np
import matplotlib.pyplot as plt

def du(l, k, dl, dk):
    u = 2 * l * k[0] * 1000
    du = ((dl/l)**2 + (dk/k[0])**2)**0.5 * u
    return du

f1 = np.array([3.219, 6.431, 9.672, 12.654, 16.171])
f2 = np.array([4.131, 8.276, 12.395, 16.522, 20.649])
f3 = np.array([4.238, 8.481, 12.712, 16.957, 21.179])
n = np.array([1, 2, 3, 4, 5])
k1 = np.polyfit(n, f1, 1)
f1 = np.polyval(k1, n)
k2 = np.polyfit(n, f2, 1)
f2 = np.polyval(k2, n)
k3 = np.polyfit(n, f3, 1)
f3 = np.polyval(k3, n)
lm = 0.604
lst = 0.605
ld = 0.605
dl = 0.0005

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.plot(n, f1, label='Медь', color='orange', linewidth=0.8)
ax.plot(n, f2, label='Сталь', color='black', linewidth=0.8)
ax.plot(n, f3, label='Дюраль', color='#8A9597', linewidth=0.8)

ax.legend(loc='upper left', fontsize=10)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([0, 6, 0, 22])

fig.subplots_adjust(bottom=0.15, left=0.2)

ax.set_title('Зависимость частоты f от номера гармоники n', loc='center', fontsize=15)
ax.set_ylabel('Частота [кГц]', loc='center', fontsize=10)
ax.set_xlabel('Номер гармоники', loc='center', fontsize=10)

plt.text(3, 5, 'Медь: $u_м$ = {:.1f}$\pm${:.1f} [м/c]\nСталь: $u_с$ = {:.1f}$\pm${:.1f} [м/c]\nДюраль: $u_д$ = {:.1f}$\pm${:.1f} [м/c]'.format(
    2 * lm * k1[0] * 1000, du(lm, k1, dl, 0.001), 2 * lst * k2[0] * 1000, du(lst, k2, dl, 0.001), 2 * ld * k3[0] * 1000, du(ld, k3, dl, 0.001)), backgroundcolor='white')

plt.show()

fig.savefig("1.4.8_harmony.png", dpi=1000)
