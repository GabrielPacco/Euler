import numpy as np
import matplotlib as plt

a = 0
b = 2
c = 1
f = (lambda x, y: x+y)
N = 100
def Euler(f, a, b, c, N):
    x = np.linspace(a, c, N)
    y = np.zeros(N)
    y[0] = b
    for i in range(N-1):
        y[i+1] = y[i] + f(x[i], y[i])*(x[i+1]-x[i])
    return x, y

"Graficando"
def graficar(x, y):
    plt.plot(x, y, 'r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Euler')
    plt.show()
