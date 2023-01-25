import numpy as np
import matplotlib.pyplot as plt

F0  = np.zeros(40)
STD = np.zeros(40)
dim = 5
vector_optimo = np.array([-2.9035, -2.9035, -2.9035, -2.9035, -2.9035])

def f(x):
	D = len(x)
	f = 0
	for i in range(D):
		f += x[i]**4 - 16*(x[i]**2) + 5*x[i]
	return (1/D)*f

for i in range(0,40):
	path = 'Resultado_BAL_'+str(i+1)+".txt"
	data = np.genfromtxt(path)
	if dim ==2:
		F0[i] = np.min(data[:,3])
		STD[i] = np.std(data[:,3])
	else:
		F0[i] = np.min(data[:,6])
		STD[i] = np.std(data[:,6])

indice_peor  = np.argmax(F0)
indice_mejor = np.argmin(F0)

Peor_solucion  = np.genfromtxt('Resultado_BAL_'+str(indice_peor + 1)+".txt")
Mejor_solucion = np.genfromtxt('Resultado_BAL_'+str(indice_mejor + 1)+".txt")
Optimo = f(vector_optimo)

Diferencia_relativa = np.min(F0) - Optimo
intervalo_menor = np.mean(F0) - 2.023*np.sqrt(np.var(F0) / 40)
intervalo_mayor = np.mean(F0) + 2.023*np.sqrt(np.var(F0) / 40)
intervalo = np.array([intervalo_menor, intervalo_mayor])

print("La mejor solución usando el algoritmo BAL: ",np.min(F0))
print("Se encuentran en las coordenadas: ", Mejor_solucion[-1,:][1:dim+1] ,"\n")

print("La peor solución usando el algoritmo BAL:",  np.max(F0))
print("Se encuentran en las coordenadas: ", Peor_solucion[-1,:][1:dim+1], "\n")

print("El promedio de los valores de la función objetivo: ", np.mean(F0))
print("La desviación estándar de los valores de la función objetivo: ", np.std(F0))
print("La diferencia relativa de esta ejecución es: ", Diferencia_relativa)
print("El intervalo de confianza de la ejecución es: ", intervalo)

eje_x = np.arange(0, Mejor_solucion[-1,0])
eje_y = np.zeros(int(Mejor_solucion[-1,0]))

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
plt.title(r'Algoritmo BAL 5D: espacio de solución')
plt.xlabel("Iteración")
plt.ylabel("FO")
plt.tight_layout()
plt.savefig("Grafico_Convergencia_BAL_5D.png")