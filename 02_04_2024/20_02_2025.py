import numpy as np # operaciones
import matplotlib.pyplot as plt #graficas

#Entradas
n=np.linspace(1,50,50) #valores en x
bigo_1= np.ones_like(n)
bigo_n=n
bigo_logn=np.log2(n)
bigo_n2=n*n
bigo_nlog2=n*np.log2(n)

#Aqui voy a creear una figura
plt.figure(figsize=(10,6))

plt.plot(n,bigo_1, label='$O(1)$',linestyle=":", color="green")# tamaño de linea = linewidth=4 # caracteristicas de la grafica
plt.plot(n,bigo_n, label='$O(n)$',linestyle=":", color="blue")# tamaño de linea = linewidth=4 # caracteristicas de la grafica
plt.plot(n,bigo_logn, label='$O(long_2 n)$',linestyle=":", color="black")# tamaño de linea = linewidth=4 # caracteristicas de la grafica
plt.plot(n,bigo_n2, label='$O(n^2)$',linestyle=":", color="pink")# tamaño de linea = linewidth=4 # caracteristicas de la grafica
plt.plot(n,bigo_nlog2, label='$O(n \cdot long_2 n)$',linestyle=":", color="purple")# tamaño de linea = linewidth=4 # caracteristicas de la grafica


plt.yscale('log')
plt.title('Notación Big O')
plt.xlabel('Tamaño de la entrada ($n$)')
plt.ylabel('Numero de operaciones')
plt.grid()
plt.legend()



plt.show()#MUESTRA LAfigura del tamaño indicado

print(n)
print(bigo_1)

##exponencial y factorial