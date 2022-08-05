import math as mat
import numpy as np
import matplotlib.pyplot as plt

def serieSen(x,N):
    s=0
    for i in range(N):
        s=s+((-1)**i)*x**(2*i+1)/mat.factorial(2*i+1)
    return s

def sumaParcial(N,p):
    s=0
    for i in range(N):
        s=s+1/i**p
    return s

x=np.linspace(0,4*mat.pi,2000)
for i in range(4,16,4):
    y=serieSen(x,i)
    plt.plot(x,y,'k')
    plt.grid(True)

y=np.sin(x)
plt.grid(True)
plt.plot(x,y,'r')
plt.axis([0,4*mat.pi,-1,1])
plt.show()