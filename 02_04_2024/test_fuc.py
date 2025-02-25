def algoritmo(x,y,z):
    print(f'x:{x}, y:{y}, z:{z}')
def medir_algo(funcion,*argumentos):
        funcion(*argumentos)
medir_algo(algoritmo,10,15,20)

#pruebas de append
#Append: Agregar al final
a=[]
print(f'a: {a}')

a.append(100)
print(f'a: {a}')

a.append(11)
print(f'a: {a}')