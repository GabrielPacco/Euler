import numpy as np
import math
import matplotlib.pyplot as plt

def funcion(x,y):
    ec = 2*(x*y)
    return ec

# Solución Exacta
def Y(x):
    ex = np.exp((x**2)-1)
    return ex

# Valores iniciales
a = 1
b = 4
c = 1

n = 200

h = (b-a)/(n-1)
x = np.zeros([n])
y = np.zeros([n])

y[0]=c
x[0]=a

for i in np.arange(0,n-1):
    x[i+1] = x[i]+h
    y[i+1] = y[i]+h*funcion(x[i],y[i])

plt.grid(True)
plt.plot(x,y,'o')

for i in np.arange(0,n-1):
    x[i+1] = x[i]+h
    z = y[i]+h*funcion(x[i],y[i])
    y[i+1] = y[i]+((funcion(x[i],y[i])+(funcion(x[i],z)))/2)*h

plt.grid(True)
plt.plot(x,y,'o')
plt.plot(x,Y(x),'*')
plt.title("Euler's Method")
plt.show()