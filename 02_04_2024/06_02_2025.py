from Analisis_de_Algoritmos.algoritmos import producto_iterativo, producto_recursivo, suma_iterativa, suma_recursiva
from Analisis_de_Algoritmos.Evaluaciones import evaluar_resultado
from Analisis_de_Algoritmos.complejidad import medir_tiempo

arr_10 = [2 for i in range(1,10+1)]
arr_250 = [2 for i in range(1,250+1)]
arr_500 = [2 for i in range(1,500+1)]





#Evalua si producto_iterativo es correcto
evaluar_resultado(producto_iterativo(arr_10), 2**10)
evaluar_resultado(producto_iterativo(arr_250), 2**250)
evaluar_resultado(producto_iterativo(arr_500), 2**500)

#Evalua si producto_recursivo es correcto
evaluar_resultado(producto_recursivo(arr_10), 2**10)
evaluar_resultado(producto_recursivo(arr_250), 2**250)
evaluar_resultado(producto_recursivo(arr_500), 2**500)

#Medir memoria de producto_iterativo
print('Memoria de producto_iterativo()')
medir_tiempo(suma_iterativa, arr_10)
medir_tiempo(suma_iterativa, arr_250)
medir_tiempo(suma_iterativa, arr_500)

#Medir memoria de producto_recursivo
print('Memoria de producto_recursivo()')
medir_tiempo(suma_recursiva, arr_10)
medir_tiempo(suma_recursiva, arr_250)
medir_tiempo(suma_recursiva, arr_500)

#Evalua si producto_iterativo es correcto
evaluar_resultado(producto_iterativo(arr_10), 2**10)
evaluar_resultado(producto_iterativo(arr_250), 2**250)
evaluar_resultado(producto_iterativo(arr_500), 2**500)