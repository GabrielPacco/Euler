# Código Python para encontrar la aproximación
# de una ecuación diferencial ordinaria
# utilizando el método de Euler.
from turtle import end_fill
import numpy as np
import math
import matplotlib.pyplot as plt

def func( y, t ):
	return y+t
# Solución exacta
def Y(t):
	return 2*np.exp(t)-t-1

# Valores iniciales
a=0
b=2
c=1
n=100

h= (b-a)/(n-1)
t=np.zeros((n))
y=np.zeros((n))
y[0]=c
t[0]=a
# Valor de x al que necesitamos aproximación

for i in np.arange(1,n):
	t[i]=t[i-1]+h
	y[i]=y[i-1]+func(y[i-1],t[i-1])*h
	

# Graficando
plt.grid(True)
plt.plot(t,y, '*')
plt.plot(t,Y(t), 'r')
#tt = np.linspace(a,0.1,b)
#yy = Y(tt)
#plt.plot(tt,yy, 'r')
plt.show()
