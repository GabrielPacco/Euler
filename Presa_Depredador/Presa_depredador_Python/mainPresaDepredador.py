import numpy as np
import matplotlib.pyplot as plt

# Presa_Depredador
alpha = 0.8
betha = 0.4
delta = 0.3
gamma = 0.6

def f(t,x,y):
    return x*(alpha-betha*y)

def g(t,x,y):
    return y*(delta*x-gamma)

a=0
b=40
x0=15
y0=4
N=300

# Construyecdo Nodos
h=(b-a)/(N-1)
tv=np.zeros([N])
tv[0]=a
for i in range(1,N):
    tv[i]=tv[i-1]+h

# Euler para sistemas de ecuaciones
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
    return y,z

# RK4 para sistemas de ecuaciones
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
    return x,y,z


# Gráfica de la solución
plt.grid(True)

[xv,yv]=EulerSist(tv,f,g,x0,y0)
plt.plot(tv,xv,'*b')
plt.plot(tv,yv,'*r')

[xq,yq,zq]=RK4(tv,f,g,x0,y0)
plt.plot(tv,yq,'*k')
plt.plot(tv,zq,'*g')
plt.show()



