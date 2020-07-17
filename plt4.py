import matplotlib.pyplot as plt
import numpy as np

c = 3e8

v = np.linspace(0,3e8,100) 

k = 1/np.sqrt(1-v**2/c**2) # Lorentz factor

plt.title("Lorentz factor - Velocity Graph")
plt.plot(v,k)
plt.xlabel("Velocity (m/s)")
plt.ylabel("Lorentz factor")
plt.show()
