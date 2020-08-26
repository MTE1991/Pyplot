import matplotlib.pyplot as plt
import numpy as np

n_0 = 6.023 # initial amount of active substance
decay_const = 1.216 # per year
t = np.linspace(0,57000,500) # carbon 14 half life ~5700 yrs
n = n_0*np.exp(-decay_const*t)

fig, ax = plt.subplots()
ax.plt(t,n)
plt.title("Radioactive Decay of Carbon-14")
plt.xlabel("time (years)")
plt.ylabel("No. of atoms present (x$10^{23}$)")
plt.show()
