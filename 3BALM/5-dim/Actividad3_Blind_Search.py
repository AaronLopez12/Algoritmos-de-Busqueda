import numpy as np
import matplotlib.pyplot as plt

sigma 		 = np.sqrt(3)
Iteraciones  = 1250

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

b0 = np.array([0, 0, 0, 0, 0])
x0 = np.array([4.0, 6.4, 4.0, 6.4, 4.0])


file = open('Resultado_BALM_iter.txt', 'w+')


for i in range(Iteraciones):
	valor_inicio = f(x0)

	if len(x0)== 2 :
		vector_random  = np.random.normal(0,sigma, 2)
	
	else:
		vector_random  = np.random.normal(0,sigma, 5)

	vector_actual = x0 + b0 + vector_random
	valor_actual  = f(vector_actual)

	if(valor_actual < valor_inicio):
		x0 = vector_actual
		b0 = 0.2*b0 + 0.4*vector_random  
		string = str(i)+"\t"+str(round(vector_actual[0],2))+ "\t"+str(round(vector_actual[1],2))+"\t"
		
		if len(x0) > 2:
			string += str(round(vector_actual[2],2))+ "\t"+str(round(vector_actual[3],2))+"\t"+ str(round(vector_actual[4],2)) + "\t"
		string += str(round(valor_actual,2))+"\n"
		file.write(string)

	else:
		vector_actual = x0 + b0 - vector_random
		valor_actual = f(vector_actual)

		if valor_actual < valor_inicio:
			x0 = vector_actual
			b0 = b0 - 0.4*vector_random
			string = str(i)+"\t"+str(round(vector_actual[0],2))+ "\t"+str(round(vector_actual[1],2))+"\t"
		
			if len(x0) > 2:
				string += str(round(vector_actual[2],2))+ "\t"+str(round(vector_actual[3],2))+"\t"+ str(round(vector_actual[4],2)) + "\t"
			string += str(round(valor_actual,2))+"\n"
			file.write(string)
		
		else:
			x0 = x0
			b0 = 0.5*b0
file.close()