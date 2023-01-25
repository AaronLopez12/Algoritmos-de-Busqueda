import numpy as np
import matplotlib.pyplot as plt

XX = np.arange(-4, 4, 0.05)
YY = np.arange(-4, 4, 0.05)
XX1 = np.arange(-8, 8, 0.05)
YY1 = np.arange(-8, 8, 0.05)

F0  = np.zeros(40)
STD = np.zeros(40)
dim = 2
vector_optimo = np.array([-2.9035, -2.9035])

def plot2D(X,Y):
	XXYY = np.meshgrid(X,Y)
	ZZ = f(XXYY)
	contours = plt.contour(X,Y,ZZ, 10)
	plt.clabel(contours, inline=True, fontsize=8)

def f(x):
	D = len(x)
	f = 0
	for i in range(D):
		f += x[i]**4 - 16*(x[i]**2) + 5*x[i]
	return (1/D)*f

for i in range(0,40):
	path = 'Resultado_BALM_'+str(i+1)+".txt"
	data = np.genfromtxt(path)
	if dim == 2:
		F0[i] = np.min(data[:,3])
		STD[i] = np.std(data[:,3])
	else:
		F0[i] = np.min(data[:,6])
		STD[i] = np.std(data[:,6])

indice_peor  = np.argmax(F0)
indice_mejor = np.argmin(F0)
print(indice_mejor)

Peor_solucion  = np.genfromtxt('Resultado_BALM_'+str(indice_peor + 1)+".txt")
Mejor_solucion = np.genfromtxt('Resultado_BALM_'+str(indice_mejor + 1)+".txt")
Optimo = f(vector_optimo)

Diferencia_relativa = np.min(F0) - Optimo
intervalo_menor = np.mean(F0) - 2.023*np.sqrt(np.var(F0) / 40)
intervalo_mayor = np.mean(F0) + 2.023*np.sqrt(np.var(F0) / 40)
intervalo = np.array([intervalo_menor, intervalo_mayor])

print("La mejor solución usando el algoritmo BALM: ",np.min(F0))
print("Se encuentran en las coordenadas: ", Mejor_solucion[-1,:][1:dim+1] ,"\n")

print("La peor solución usando el algoritmo BALM:",  np.max(F0))
print("Se encuentran en las coordenadas: ", Peor_solucion[-1,:][1:dim+1], "\n")

print("El promedio de los valores de la función objetivo: ", np.mean(F0))
print("La desviación estándar de los valores de la función objetivo: ", np.std(F0))
print("La diferencia relativa de esta ejecución es: ", Diferencia_relativa)
print("El intervalo de confianza de la ejecución es: ", intervalo)

plt.arrow(4.0, 6.4, Mejor_solucion[0,1]-4.0, Mejor_solucion[0,2] - 6.4, head_width = 0.1, 
			color = 'r', linestyle = "--")

plot2D(XX,YY)
plot2D(XX1,YY1)
for i in range(len(Mejor_solucion)-1):
	punto_inicial_x = Mejor_solucion[i,1]
	punto_inicial_y = Mejor_solucion[i,2]
	punto_final_x   = Mejor_solucion[i+1,1]
	punto_final_y   = Mejor_solucion[i+1,2]
	delta_x = punto_final_x - punto_inicial_x
	delta_y = punto_final_y - punto_inicial_y
	plt.arrow(punto_inicial_x, punto_inicial_y, delta_x, delta_y, head_width = 0.1, 
		color = 'r', linestyle = "--")

plt.ylim(-8,8)
plt.xlim(-8,8)
plt.title(r'Algoritmo BALM 2D: espacio de solución')
plt.xlabel(r'$x_{1}$')
plt.ylabel(r'$x_{2}$')
plt.tight_layout()
plt.savefig('3BALM.png')
plt.clf()

eje_x = np.arange(0, np.max(Mejor_solucion[-1,0]), 1)
eje_y = np.zeros(int(np.max(Mejor_solucion[-1,0])))


if Mejor_solucion[0,0] == 0:
	for i in range(len(Mejor_solucion)-1):
		dif = Mejor_solucion[i+1,0] - Mejor_solucion[i,0]
		indice_m = int(Mejor_solucion[i,0])
		indice_M = int(Mejor_solucion[i,0]) + int(dif)
		eje_y[indice_m: indice_M] = Mejor_solucion[i,-1]
		
else:
	eje_y[0: int(Mejor_solucion[0,0])] = Mejor_solucion[0,-1]
	for i in range(1,len(Mejor_solucion)):
		dif = Mejor_solucion[i,0] - Mejor_solucion[i-1,0]
		indice_m = int(Mejor_solucion[i-1,0])
		indice_M = int(Mejor_solucion[i,0])
		eje_y[indice_m: indice_M] = Mejor_solucion[i,-1]

plt.plot(eje_x,eje_y, color = 'red')
plt.grid()
plt.title(r'Algoritmo BALM 2D: espacio de solución')
plt.xlabel("Iteración")
plt.ylabel("FO")
plt.tight_layout()
plt.savefig("Grafico_Convergencia_BALM_2D.png")
