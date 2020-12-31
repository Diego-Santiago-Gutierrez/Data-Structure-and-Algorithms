import random
from time import perf_counter 
import sys
import math


def BusqLineal(A, x): #Recibe un arrleglo A y X que es el elemento a buscar 
    for k in (A): #Recorremos el arreglo A para ir realizando la busqueda
        if A[k] == x: #If A en la posicion k es igual a X
            return k #Te regresara K que es la posicion del arreglo 
    return "No existe" #Si no se encontró nada regresa un none 

def BusqBinRec(A, x, izq, der): #Busqueda binaria recibe el arreglo, el elemento a buscar, el inicio del arreglo y el final del mismo.
    if izq>der: #Si izquierda es mayor a derecha , quiere decir que el arreglo no esta lleno o tiene un elemento 
        return izq # Regresa un menos uno . es decir un none 

    medio = (izq+der)//2 #Sacamos el medio del arreglo  
    if x == A[medio]: # Si el valor x que estamos buscando es igual al elemento del medio 
        return medio #Se retornara el valor del medio (indice)
    
    if x > A[medio]: #Si el valor que buscamos es mayor al valor del medio, se buscara por el lado derecho
        return BusqBinRec(A, x, medio+1, der) #Retoramos el valor de la funcion pero ahora dandole el valor del inicio, se le da la mitad del arreglo y buscará hasta el final del mismo
    else:
        return BusqBinRec(A, x, izq, medio-1) #De lo contrario se buscara del medio a la izquierda del programa 

# Wrapper de búsqueda binaria modificada
# Esta versión retorna el índice donde el elemento
# debería estar, en caso de no encontrarse
def BinarioModificacion(A, x):
    return BusqBinRec(A, x,  0, len(A) - 1)

def findClosestNeighbors(A, num, max, busqueda):
   
    A = A.copy() # hacemos una copia del arreglo
    A.sort()  # Arreglamos el arreglo en caso de no estarlo
    index = BinarioModificacion(A, busqueda) #Copiamos el indice del valor devuelto 
    vecinos = [] #Creamos el arreglo con el que llenaremos de vecinos 

    def distancias(idx):              #Calculamos las distancias si son menor al radio
        return abs(A[idx] - busqueda) #Regresamos el valor de dicha operacion 

    leftPointer = index - 1 #Elemento por la izquierda
    rightPointer = index #Elemento por la derecha 

    # Diferencia entre los elementos anteriores
    # y el elemento buscado
    difDer = distancias(rightPointer) #Calculamos la distancia del puntero a la derecha
    difIzq = math.inf #Sacamos math.ing a difIzq
    if leftPointer >= 0: #Si el puntero es mayor a 0
        difIzq = distancias(leftPointer) #difIzq será la distancia que hay con el punteroizquierdo

    while len(vecinos) < num and (difIzq <= max or difDer <= max): 
    #Si el tamaño de vecinos es menor al numero }
    #Solicitado y que sean menor o mayor al rango por izq o derecha 
    #ambos vecinos candidatos están dentro del rango

       
        if difIzq <= difDer:  # La distancia al vecino izquierdo es menor o igual
            vecinos.append(A[leftPointer]) #Insertas el valor en el arreglo
            leftPointer -= 1 #Recorres un valor a la izquierda 

            if leftPointer == -1: #Si te sales del arreglo
                difIzq = math.inf #invalidas el lado 
            else:
                difIzq = distancias(leftPointer) #La diferencia de la distancia con el puntero izquierda
        
        else: # La distancia al vecino derecho es mayor
            vecinos.append(A[rightPointer]) #Insertar el valor que se encuentra en el puntero derecho a vecinos
            rightPointer += 1 #Incrementas el valor 

            if rightPointer == len(A): #si se llega al final
                difDer = math.inf #invalidas el valor
            else:
                difDer = distancias(rightPointer) #Regresas el valor de la distancai con respecto al puntero derecha 

    vecinos.sort() #Acomodas el arreglo
    return vecinos #Retornas el valor 



    
############################################################

n = 1000000
listaAleatoria = []

for i in range(n):
    listaAleatoria.append(random.randint(0, n/2))

comparaciones = 0

aleatoriaA = listaAleatoria[:]
aleatoriaB = listaAleatoria[:]


k = int(input("¿Qué elemento deseas buscar?\n")) #Llave que vamos a buscar

#-----Busqueda Binaria-------# 
aleatoriaA.sort() #Ordenamos sus datos
t0 = perf_counter() #Tiempo uno
a = BusqBinRec(aleatoriaA, k, 0, len(aleatoriaA)-1) #Ejecutamos la función
t1 = perf_counter()

print("BUSQUEDA BINARIA")
if not a:
    print("\tEl elemento", k, "no es parte del arreglo.")
else:
    print("\tEl numero: ", k, " indice: ", a )

print("\tTiempo busqueda Binaria: {0:f} segundos", (t1 - t0))
print("\tn: ", n, "\n")

#--------Busqueda Lineal--------#
aleatoriaB.sort()
t0 = perf_counter()
b = BusqLineal(aleatoriaB, k)
t1 = perf_counter()

print("BUSQUEDA LINEAL ")
if not b:
    print("\tEl elemento", k, "no es parte del arreglo.")
else:
    print("\tEl numero: ", k, " indice: ", b )

print("\tTiempo busqueda Binaria: {0:f} segundos", (t1 - t0))
print("\tn: ", n, "\n")

#-------ENCONTRAR VECINOS---------#
c=[10, 30, 60, 72, 80, 82, 84, 85, 86, 88, 90, 91, 92, 94, 97, 100]
d=[3, 5, 22, 40,42, 43, 45, 47, 55]

print(findClosestNeighbors(c, 10, 10, 84))
print(findClosestNeighbors(d, 5, 2, 41.5))

#######################################################
