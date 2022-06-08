# Código Python para encontrar la aproximación
# de una ecuación diferencial ordinaria
# utilizando el método de Euler.
import numpy as np
import matplotlib.pyplot as plt
# Consideremos una ecuación diferencial
# dy / dx =(x + y + xy)
def func( y, t ):
	return (t + y + t*y)

# Solución exacta
def Y(t):
	return 2*np.exp(t)-t-1

# Función para la fórmula de Euler
def euler( x0, y, h, x ):
	temp = -0

	# Iterando hasta el punto en el que
	# necesitamos la aproximación
	while x0 < x:
		temp = y
		y = y + h * func(x0, y)
		x0 = x0 + h
		print("x =", x0, "y =", y)

	# Impresión de la aproximación
	print("Approximate solution at x = ", x, " is ", "%.6f"% y)
	
# Código del conductor
# Valores iniciales
x0 = 0
y0 = 1
h = 0.025

# Valor de x al que necesitamos aproximación
x = 0.1

euler(x0, y0, h, x)

# Graficando
plt.grid(True)
plt.plot(x0,y0, '*')
plt.plot(x0,Y(x0), 'r')

plt.show()
