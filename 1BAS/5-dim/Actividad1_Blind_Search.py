import numpy as np
import matplotlib.pyplot as plt

def f(x):
	D = len(x)
	f = 0
	for i in range(D):
		f += x[i]**4 - 16*(x[i]**2) + 5*x[i]
	return (1/D)*f

def plot2D():
	XX = np.arange(-4, 4, 0.005)
	YY = np.arange(-4, 4, 0.005)
	XXYY = np.meshgrid(XX,YY)
	ZZ = f(XXYY)
	contours = plt.contour(XX,YY,ZZ, 10)
	plt.clabel(contours, inline=True, fontsize=8)


x0 = np.array([4.0, 6.4, 4.0, 6.4, 4.0])

Iteraciones  = 1250	# Iteraciones  
valor_inicio = f(x0)

file = open('Resultado_BAS_iter.txt', 'w+')
for i in range(Iteraciones):
	if len(x0) == 2:
		vector_random  = [np.random.uniform(-8,8), np.random.uniform(-8,8)]
	
	else:
		vector_random  = [np.random.uniform(-8,8), np.random.uniform(-8,8),
						  np.random.uniform(-8,8), np.random.uniform(-8,8),
						  np.random.uniform(-8,8)]

	valor_random = f(vector_random)
	if (valor_random < valor_inicio):
		valor_inicio = valor_random
		string = str(i)+"\t"+str(round(vector_random[0],2))+ "\t"+str(round(vector_random[1],2))+"\t"
		if len(x0) > 2:
			string += str(round(vector_random[2],2))+ "\t"+str(round(vector_random[3],2))+"\t"+ str(round(vector_random[4],2)) + "\t"
		string += str(round(valor_random,2))+"\n"
		file.write(string)

file.close()