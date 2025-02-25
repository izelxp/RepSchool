from Analisis_de_Algoritmos.algoritmos import suma_iterativa,suma_recursiva
from Analisis_de_Algoritmos.complejidad import medir_tiempo
from Analisis_de_Algoritmos.Evaluaciones import evaluar_resultado
#from Analisis_de_Algoritmos.algoritmos import producto_iterativo, producto_recursivo

arr_10 = [i for i in range(1,10+1)]
arr_250 = [i for i in range(1,250+1)]
arr_500 = [i for i in range(1,500+1)]


#Evalua si la suma iterativa es correcta
evaluar_resultado(suma_iterativa(arr_10), 55)
evaluar_resultado(suma_iterativa(arr_250), 31375)
evaluar_resultado(suma_iterativa(arr_500), 125250)

#Evalua si suma recursiva es correcta
evaluar_resultado(suma_recursiva(arr_10), 55)
evaluar_resultado(suma_recursiva(arr_250), 31375)
evaluar_resultado(suma_recursiva(arr_500), 125250)

#Medir tiempos de suma_iterativa
print('Tiempos de suma_iterativa()')
medir_tiempo(suma_iterativa, arr_10)
medir_tiempo(suma_iterativa, arr_250)
medir_tiempo(suma_iterativa, arr_500)

#Medir tiempos de suma_recursiva
print('Tiempos de suma_recursiva()')
medir_tiempo(suma_recursiva, arr_10)
medir_tiempo(suma_recursiva, arr_250)
medir_tiempo(suma_recursiva, arr_500)