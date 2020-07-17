import numpy as np  
import matplotlib.pyplot as plt  

def graph(formula, x_range):
    c = 3e8  
    v = np.array(x_range)  
    y = eval(formula)
    plt.plot(v, y)  
    plt.show()

graph('1/(v**2/c**2)', range(0, 300000000))