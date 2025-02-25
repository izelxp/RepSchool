import numpy as np # operaciones
import matplotlib.pyplot as plt #graficas


print(np.cos(10))
print(np.ones(10))
print(np.ones_like(10))
print(np.ones_like([10,2,5]))
matriz1=np.array([[1,2],[3,4]])
matriz2=np.array([[5,6],[7,8]])
suma=matriz1+matriz2
print(matriz1)
print(matriz2)
print(suma)
print(np.ones_like(10))
print(np.ones_like(matriz1))
vector=np.array([10,7,2,1,9])
print(vector)
print(np.cos(vector))

#actividad

arr=np.linspace(0,10,1)
arr1=np.linspace(1,4,7)
print(arr)
print(arr1)

############################################3

#Aqui voy a creear una figura
plt.figure(figsize=(10,6))

plt.show()#Nueva figura del tamaño indicado


'''
iport matplotlib.pyplot as plt
'''