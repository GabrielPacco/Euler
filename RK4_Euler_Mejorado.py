import numpy as np
import math
import matplotlib.pyplot as plt

# Valores iniciales
a=0
b=2
y0=1
N=10


def f(x,y):
    return x+y

# Solución exacta
def y1(x):
    ec=-1-x+(2*np.exp(x))
    return ec

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

# Función para RK4
def RK4(x,f,y0):
    n=len(x)
    y=np.zeros([n])
    y[0]=y0
    for i in range(n-1):
        h = x[i+1]-x[i]
        p = f(x[i],y[i])*h
        q = f(x[i]+h/2,y[i]+p/2)*h
        r = f(x[i]+h/2,y[i]+q/2)*h
        s = f(x[i]+h,y[i]+r)*h

        y[i+1] = y[i] + (p+2*q+2*r+s)/6
    return y


h=(b-a)/(N-1)
xv=np.zeros([N])
xv[0]=a
for i in range(1,N):
    xv[i]=xv[i-1]+h

# Grafica de Euler Tradicional
plt.grid(True)
plt.plot(xv,Euler(xv,f,y0),'*c')

#Grafica de Euler Mejorado
plt.grid(True)
plt.plot(xv,Heun(xv,f,y0),'*g')

#Grafica de RK4
plt.grid(True)
plt.plot(xv,RK4(xv,f,y0),'*k')

#Grafica de solución exacta
plt.plot(xv,y1(xv),'r') #Solución exacta
plt.title("Euler RK4")
plt.show()