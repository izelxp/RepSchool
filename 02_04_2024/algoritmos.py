
#Algoritmo íterativO (abra varios for o uno)


def suma_iterativa(arr):
    suma=0
    for val in arr:
        suma+=val
    return suma
'''*******************************************************************
#Algortmo:Suma recursiva
#Entrada: Arreglo "arr" de números enteros
Salida:Resultado de la suma de elementos suma
Paso1: Iniciar
Paso 2: Si ela rreglo "arr" no tiene ningun elemento: (Condicion de para de recursividad)
    Devuelve cero
    ir a Paso 4
Paso 3: Devolver el valor del primer elemento de "arr" mas el resultado de la Suma
Recursiva del resto de los elementos de "arr"
Paso 4: Finalizar
'''
#Algoritmo recursivo de suma
def suma_recursiva(arr):
    if len(arr) ==0 : #si el tamaño del arreglo es cero
        return 0
    return arr[0]+ suma_recursiva(arr[1:])# quiero desde el primer elemento hasta el resto "1:"


'''
*******************************************************************************
#Algortmo:Producto iterativo
#Entrada: Arreglo "nums" de números enteros
Salida:Producto de los elementos en "nums"
Paso1: Iniciar
Paso 2:Inicio "producto" en 1
Paso 3: Para cada elemento en "nums"
    3.1: Multiplica "producto" por "elemento" y asigns el resultado a "producto"
Paso 4: Devolver el producto
Paso 4: Finalizar
'''
#Algoritmo iterativo de producto
def producto_iterativo(nums):
    producto=1
    for elem in nums:
        producto*=elem  #producto=producto*elem
    return producto


'''
*******************************************************************
#Algortmo:Producto recursiva
#Entrada: Arreglo "nums" de números enteros
Salida:"Producto" de los elements en "nums"
Paso1: Iniciar
Paso 2: Si "num" no tiene elementos: (Condicion de para de recursividad)
    Devuelve cero
    ir a Paso 4
Paso 3: Devolver el valor del primer elemento de "nums" multimplicado por el resultado de 
"Producto recursivo" sobre el resto de los elementos en "nums"
Paso 4: Finalizar
'''
#Algoritmo recursivo de producto
def producto_recursivo(nums):
    if len(nums)== 0:
        return 1
    return nums[0]* producto_recursivo(nums[1:])



# Algoritmo factorial_iterativo
def factorial_iterativo(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# Algoritmo factorial_recursivo
def factorial_recursivo(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial_recursivo(num - 1)


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

(4n+2)



'''
#Algoritmo de producto escalar
def producto_escalar(v1,v2):
    p=[] #arreglo vacio #1 asignacion
    for e1, e2 in zip(v1,v2): #1 funcion + n accesos +n accesos =2n+1
        p.append(e1 * e2) # n operaciones + n funciones = 2n
    return p # 1 retorno
    # (4n + 3)
#Algoritmo de producto escalar (version 2 estilo c++)
def producto_escalar_v2(v1,v2):
    p = []  # arreglo vacio #1 asignacion
    n=len(v1)# 1 funcion + 1 asignacion
    for i in range(n):
        p.append(v1[i]* v2[i]) #n operaciones + n funciones + n accesos + n accesos
    return p # 1 retorno
#(5n+5)

    #nota el append sirve para agrega el valor de cada elemento

'''
float * producto_escalar(float *v1, float *v2, int n {
    float *p=(float *)malloc(sizeof(float)* n); //1 asignación
    //+ 2funciones + 1 producto =4
      
    for(int i = 0; i <n ; i++){//1 asignacion + n comparaciones + n sumas
        //= 2n+1
        p[i]=v1[i], v2[i];//3n accesos a arreglo + n asignaciones
        // + n productos=5n
    }
    return p; // 1 retorno
}

// 7n + 6
'''

'''
Alg. Suma matrices
Entrada: Matrices "m1" y "m2"
Salida: Suma "s"
P1: Iniciar
P2 Inicio "s" como matriz vacia #1 asignacion
P3: Para "ren1" y "ren2"
m1=[]
'''

def sumar_matrices(m1,m2):
    s=[] #1 asignación
    for ren1, ren2 in zip(m1,m2): # 1 funcion +n accesos + n accesos =2n+1
        #Nota: lo de abajo se repite n veces
        ren=[]# n*1 asignacion = n
        for e1, e2 in zip(ren1,ren2): #n *(1 funcion + n accesos + n accesos)=2n^2+n
            #Nota lo de abajo se repite n*n veces = n^2 veces
            ren.append(e1+ e2) #agrega valores a un areglo #n^2*(1 suma + 1 funcion)= 2n^2
        s. append(ren)# n * 1 funcion =n
    return s# 1 retorno = 1

#No. operaciones elementales = 4n^2+5n+3


def contar_distintos(a):
    c= 0 #1 asignacion
    for e in a:# n acceso
        #Nota:Lo de abajo se repite n veces
        r=0 #n *1 asignacion = n
        for e2 in a: #n * n accesos =n^2
            # Nota:Lo de abajo se repite n veces
            if e2==e: #n^2* 1 comparacion = n^2
                r+=1 #n^2*(1 suma*1 asignacion)=2n^2
        if r==1: # n*1comparacion=n
            c+=1 #n*(1 suma*1 asignacion)=2n
    return c # 1 retorno
# N0. operaciones elementasles  =4n^2 + 4n+2



def potencia_iterativa(base, exponente):
    resultado= 1
    for _ in range(exponente):
        resultado *= base
    return resultado

def potencia_recursiva(base, exponente):
    if exponente==0:
        return 1
    return base*potencia_recursiva(base, exponente-1)