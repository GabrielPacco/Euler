import matplotlib.pyplot as plt
import numpy as np

def f(n):
    return 6*n**2 + 100*n + 300

def g(n):
    return 0.6*n**2 + 1000*n + 3000

values = np.arange(0, 250, 0.1)
plt.plot(f(values))
plt.plot(g(values))
plt.show()