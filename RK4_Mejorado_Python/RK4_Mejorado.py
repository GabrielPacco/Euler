import numpy as np
import math
import matplotlib.pyplot as plt

# Valores iniciales
a=0
b=4
y0=0
z0=1
N=40


def f(t,y,z):
    return z

def g(t,y,z):
    ec= -np.sin(t)
    return ec

# Solución exacta
def y1(t):
    ec=np.sin(t)
    return ec

# Construyendo los nodos
h=(b-a)/(N-1)
tv=np.zeros([N])
tv[0]=a
for i in range(1,N):
    tv[i]=tv[i-1]+h



# Función para Euler Tradicional
def Euler(x,f,y0):
    n=len(x)
    y=np.zeros([n])
    y[0]=y0
    for i in range(n-1):
        h=x[i+1]-x[i]
        y[i+1]=y[i]+h*f(x[i],y[i])
    return y

# Función para Euler Mejorado
def Heun(x,f,y0):
    n=len(x)
    y=np.zeros([n])
    y[0]=y0
    for i in range(n-1):
        h=x[i+1]-x[i]
        z=y[i]+h*f(x[i],y[i])
        y[i+1]=y[i]+h*(f(x[i],y[i])+f(x[i+1],z))/2
    return y

# Función para EulerSist
def EulerSist(x,f,g,y0,z0):
    n=len(x)
    y=np.zeros([n])
    z=np.zeros([n])
    y[0]=y0
    z[0]=z0
    for i in range(n-1):
        h=x[i+1]-x[i]
        y[i+1]=y[i]+h*f(x[i],y[i],z[i])
        z[i+1]=z[i]+h*g(x[i],y[i],z[i])
    return y


#Grafica de Euler para sistemas de ecuaciones
plt.grid(True)
plt.plot(tv,EulerSist(tv,f,g,y0,z0),'*c')

#Grafica de la solución exacta
plt.plot(tv,y1(tv),'r')
plt.title("Euler Sist")
plt.show()


