import numpy as np
import matplotlib.pyplot as plt

# Valores iniciales
a=0
b=4
y0=0
z0=1
N=20

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

# RK para sistemas de funciones
def RK4(x, f, g, y0, z0):
    n = len(x)
    y = np.zeros([n])
    z = np.zeros([n])
    y[0] = y0
    z[0] = z0
    for i in range(n - 1):
        h = x[i + 1] - x[i]
        p1=f(x[i],y[i],z[i])*h
        q1=g(x[i],y[i],z[i])*h
        p2=f(x[i]+h/2,y[i]+p1/2,z[i]+q1/2)*h
        q2=g(x[i]+h/2,y[i]+p1/2,z[i]+q1/2)*h
        p3=f(x[i]+h/2,y[i]+p2/2,z[i]+q2/2)*h
        q3=g(x[i]+h/2,y[i]+p2/2,z[i]+q2/2)*h
        p4=f(x[i]+h,y[i]+p3,z[i]+q3)*h
        q4=g(x[i]+h,y[i]+p3,z[i]+q3)*h
        y[i+1] = y[i] + (p1+2*p2+2*p3+p4)/6
        z[i+1] = z[i] + (q1+2*q2+2*q3+q4)/6
    return x,y


#Grafica de Euler para sistemas de ecuaciones
plt.grid(True)
plt.plot(tv,EulerSist(tv,f,g,y0,z0),'*c')

#Grafica de RK4
plt.grid(True)
plt.plot(tv,RK4(tv,f,g,y0,z0)[1],'*k')


#Grafica de la solución exacta
plt.plot(tv,y1(tv),'r')
plt.title("Euler Sist")
plt.show()


