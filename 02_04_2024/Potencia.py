from Analisis_de_Algoritmos.algoritmos import potencia_iterativa, potencia_recursiva
from Analisis_de_Algoritmos.Evaluaciones import evaluar_resultado
from Analisis_de_Algoritmos.complejidad import medir_memoria_1

#valores correctos
z=base=65
a=z**10
b=z**250
c=z**500


exponente_10=10
exponente_250=250
exponente_500=500


print("\nEvalua el resultado de la potencia iterativa")
evaluar_resultado(potencia_iterativa(base,exponente_10),a)
evaluar_resultado(potencia_iterativa(base,exponente_250),b)
evaluar_resultado(potencia_iterativa(base,exponente_500),c)
print("\nEvalua el resultado de la potencia recursiva")
evaluar_resultado(potencia_recursiva(base,exponente_10),a)
evaluar_resultado(potencia_recursiva(base,exponente_250),b)
evaluar_resultado(potencia_recursiva(base,exponente_500),c)
print("\nMedir memoria de potencia iterativa")
medir_memoria_1(potencia_iterativa,base,exponente_10)
medir_memoria_1(potencia_iterativa,base,exponente_250)
medir_memoria_1(potencia_iterativa,base,exponente_500)
print("\nMedir memoria de potencia recursiva")
medir_memoria_1(potencia_recursiva,base,exponente_10)
medir_memoria_1(potencia_recursiva,base,exponente_250)
medir_memoria_1(potencia_recursiva,base,exponente_500)

