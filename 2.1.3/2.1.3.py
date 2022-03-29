import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('2.1.3.xlsx', sheet_name='Лист1')
names = list(data)
print(data)

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)

v = np.array(data[names[0]]) * 1000
v = v[np.where(v != 0)]
dl = np.array(data[names[1]]) * 0.01
dl = dl[np.where(dl != 0)]
index = np.linspace(1, len(dl), len(dl))
k= np.polyfit(index, dl, 1)
dlp = np.polyval(k, index)
ax.scatter(index, dl, label=str(v[0]), marker='.')
ax.plot(index, dlp, label='{:.3f} * k + {:.3f}'.format(k[0], k[1]))

for i in range(2, 10, 2):
    v = np.array(data[names[i]]) * 1000
    v = v[np.where(v != 0)]
    dl = np.array(data[names[i + 1]]) * 0.01
    dl = dl[np.where(dl != 0)]
    index = np.linspace(1, len(dl), len(dl))
    k, cov = np.polyfit(index, dl, 1, cov=(len(dl)!= 2))
    dlp = np.polyval(k, index)
    ax.scatter(index, dl, label=str(v[0]), marker='.')
    ax.plot(index, dlp, label='{:.3f}$\pm${:.3f} * k + {:.3f}'.format(k[0], np.sqrt(cov[0][0]), k[1]))
              
ax.legend(loc='lower right', fontsize=10)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([0, 7, 0, 0.23])

#fig.subplots_adjust(bottom=0.15, left=0.2)

ax.set_title('Зависимость удлинения трубы $dL$ от номера последовательного резонанса $k$', loc='center', fontsize=15)
ax.set_ylabel('$dL, м$', loc='center', fontsize=10)
ax.set_xlabel('$k$', loc='center', fontsize=10)

plt.show()

fig.savefig("2.1.3.png", dpi=500)
