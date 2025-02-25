#<1,2,3>.<4,5,6>=<4,10,18>
'''
Algoritmo: Producto escalar de vectores
Entradas:Arreglos "v1" y "v2" de "n" elem.
Salida:Arreglo "p" con el resultado del prodducto
P1: Iniciar
P2:Inicializar "p" como arreglo vacio  #1 asignacion
P3:Para cada elemeto "e1" y "e2" de "v1" y "v2" #n+n=2n accesos
    P3.1: Calcular producto "e1" y "e2" #n productos
    P3.2: Agregar resultado a "p" # n funciones
P4: Regresa "p" #1 retorno
P5: Fin

(4n+2)'''


#implementaciones producto escalar
from Analisis_de_Algoritmos.algoritmos import producto_escalar, producto_escalar_v2, sumar_matrices, contar_distintos
from Analisis_de_Algoritmos.Evaluaciones import evaluar_resultado

v1= [1, 2, 3]
v2= [4, 5, 6]
r= [4 ,10, 18]

evaluar_resultado(producto_escalar(v1,v2),r)
evaluar_resultado(producto_escalar_v2(v1,v2),r)

'''

Alg. Suma matrices
Entrada: Matrices "m1" y "m2"
Salida: Suma "s"
P1: Iniciar
P2 Inicio "s" como matriz vacia #1 asignacion
P3: Para "ren1" y "ren2"
m1=[]
'''
#Problema adicional 4
m1=[[1,2],
    [3,4]]
m2=[[5,6],
    [7,8]]
r=[[6,8],
   [10,12]]
# matriz en c
#float **m1 ={{,2}, {3,4}};
#print(m1[1][0])

#for ren1, ren2 in zip(m1,m2):
 #   print(f'ren1:{ren1}, ren2:{ren2}')



print(sumar_matrices(m1,m2))
evaluar_resultado(sumar_matrices(m1,m2),r)


#Problema adicional 5
a=[1,2,3,2,3,4]
r=2



print(contar_distintos(a))
evaluar_resultado(contar_distintos(a),r)