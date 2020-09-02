import matplotlib.pyplot as plt
import numpy as np

# initial amount of active substance, same for all in this scenario:
n_0 = 6.023e23

# Radioactive decay constants (1/y) for each element:
decay_u238 = 1.54e-10
decay_u235 = 9.72e-10

t = np.linspace(0,3e10,500) # years

# Remnants after a certain time (t):

n2 = n_0 * np.exp(-decay_u238 * t)
n3 = n_0 * np.exp(-decay_u235 * t)

fig, ax = plt.subplots()

ax.plot(t, n2, label="U-238")
ax.plot(t, n3, label="U-235")
ax.legend()

plt.title("Radioactive Decay of Uranium")
plt.xlabel("time ($10^{10}$ years)")
plt.ylabel("No. of atoms present (x$10^{23}$)")
plt.show()
