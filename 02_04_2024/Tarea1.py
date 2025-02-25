#10. Escriba una función en lenguaje de python que reciba un arreglo arr de valores enteros y lo devuelva ordenado
def ordenar_arreglo(arr):
    return sorted(arr)

# Ejemplo de uso
arreglo = [5, 3, 8, 1, 9, 2]
arreglo_ordenado = ordenar_arreglo(arreglo)
print(arreglo_ordenado)  # Salida: [1, 2, 3, 5, 8, 9]

#8.Escriba una función en lenguaje de python que reciba un arreglo arr de valores enteros y lo devuelva la suma de todos sus elementos
def suma_arreglo(arr):
    return sum(arr)

# Ejemplo de uso
arreglo = [5, 3, 8, 1, 9, 2]
suma_total = suma_arreglo(arreglo)
print(suma_total)  # Salida: 28

#9.Escriba una función en lenguaje de python que reciba un arreglo de valores enteros "arr" y el valor "a", y devuelva el indice donde se encuentra "a".
def encontrar_indice(arr, a):
    if a in arr:
        return arr.index(a)
    else:
        return -1

# Ejemplo de uso
arreglo = [5, 3, 8, 1, 9, 2]
valor = 8
indice = encontrar_indice(arreglo, valor)
print(indice)  # Salida: 2