import math

def BusqBinRec(A, x, izq, der): #Busqueda binaria recibe el arreglo, el elemento a buscar, el inicio del arreglo y el final del mismo.
    if izq>der: #Si izquierda es mayor a derecha , quiere decir que el arreglo no esta lleno o tiene un elemento 
        return izq # Regresa un elemento o un none

    medio = (izq+der)//2 #Sacamos el medio del arreglo  

    if x == A[medio]: # Si el valor x que estamos buscando es igual al elemento del medio 
        return medio #Se retornara el valor del medio (indice)

    if x > A[medio]: #Si el valor que buscamos es mayor al valor del medio, se buscara por el lado derecho
        return BusqBinRec(A, x, medio+1, der) #Retoramos el valor de la funcion pero ahora dandole el valor del inicio, se le da la mitad del arreglo y buscará hasta el final del mismo
    else:
        return BusqBinRec(A, x, izq, medio-1) #De lo contrario se buscara del medio a la izquierda del programa 

lista=[1,2,3,4,5,6,7,8,9,10]
a=BusqBinRec(lista, 7, 0, len(lista)-1)
print("El elemento se encuentra en el indice: ", a)

############################################################

# n = 1000000
# listaAleatoria = []

# for i in range(n):
#     listaAleatoria.append(random.randint(0, n/2))

# comparaciones = 0

# aleatoriaA = listaAleatoria[:]
# aleatoriaB = listaAleatoria[:]

# k = int(input("¿Qué elemento deseas buscar?\n")) #Llave que vamos a buscar





#######################################################