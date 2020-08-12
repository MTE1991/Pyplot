import matplotlib.pyplot as plt
import numpy as np

c = 3e8
v = np.linspace(0,2.999e8,100) 
gamma = 1/np.sqrt(1-v**2/c**2) # Lorentz factor

plt.title("Lorentz factor - Velocity Graph")
plt.plot(v,gamma)
plt.xlabel("Velocity (m/s)")
plt.ylabel("Lorentz factor $\gamma$")
plt.show()
