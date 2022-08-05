import math as mat
import numpy as np
import matplotlib.pyplot as plt

def serieExp(x,N):
    s=0
    for n in range(N):
        s=s+((mat.exp(3))/(mat.factorial(n)))*np.power((x-3),n)
    return s

def sumaParcial(N,p):
    s=0
    for i in range(N):
        s=s+1/i**p
    return s

x=np.linspace(0,4*mat.pi,2000)
for i in range(4,16,4):
    y=serieExp(x,i)
    plt.plot(x,y)
    plt.grid(True)

y=np.exp(x)
plt.grid(True)
plt.plot(x,y,'r')
plt.axis([0,4*mat.pi,-10,10])
plt.show()

#http://www.sfu.ca/math-coursenotes/Math%20158%20Course%20Notes/sec_powerseries.html