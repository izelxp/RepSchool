import math

from Analisis_de_Algoritmos.algoritmos import factorial_iterativo, factorial_recursivo
from Analisis_de_Algoritmos.Evaluaciones import evaluar_resultado
from Analisis_de_Algoritmos.complejidad import medir_tiempo


#Valores correctos
fac_10= math.factorial(10)
fac_250= math.factorial(250)
fac_500= math.factorial(500)

#Evalua si producto_iterativo es correcto
print('Evalua si factorial_iterativo es correcto)')
evaluar_resultado(factorial_iterativo(10),fac_10)
evaluar_resultado(factorial_iterativo(250),fac_250)
evaluar_resultado(factorial_iterativo(500),fac_500)
print('\n')
#Evalua si producto_recursivo es correcto
print('Evalua si factorial_recursivo es correcto)')
evaluar_resultado(factorial_recursivo(10),fac_10)
evaluar_resultado(factorial_recursivo(250),fac_250)
evaluar_resultado(factorial_recursivo(500),fac_500)
print('\n')
#Medir tiempos de factorial_iterativa
print('Tiempos de factorial_iterativa()')
medir_tiempo(factorial_iterativo, 10)
medir_tiempo(factorial_iterativo, 250)
medir_tiempo(factorial_iterativo, 500)
print('\n')#Medir tiempos de factorial_recursiva
print('Tiempos de factorial_recursiva()')
medir_tiempo(factorial_recursivo, 10)
medir_tiempo(factorial_recursivo, 250)
medir_tiempo(factorial_recursivo, 500)