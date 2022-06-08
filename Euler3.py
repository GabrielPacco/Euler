# Código Python para encontrar la aproximación
# de una ecuación diferencial ordinaria
# utilizando el método de Euler.
from turtle import end_fill
import numpy as np
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
n=10

h=(b-a)/(n-1)
#t=np.zeros(1,n)
#y=np.zeros(1,n)
y:(1)=c
t:(1)=a
# Valor de x al que necesitamos aproximación

for i in range(2,n):
	t:(i)=t[i-1]+h
	t:(i)=y[i-1]+h*func(y[i-1],t[i-1])

def graficar(x, y):
	plt.plot(x, y, 'r')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Euler')
	plt.show()

graficar(t, y)

