# importamos la primera libreria para tomar el tiempo y otra para generar numeros aleatorios
import random
from time import time
import sys

# Definimos la función llamada InsertionSort


def InsertionSort(arreglo):

    # n Será del tamaño del arreglo que reciba
    n = len(arreglo)

    # El ciclo for recorrerá de 1 al tamaño del arreglo para asegurar que todos los elementos dentro del mismo sean procesados
    for i in range(1, n):
        # se toma el valor que este dentro del arreglo en la posicion i
        val = arreglo[i]
        # J nos ayudará a separar los elementos del arreglo, en el primer caso se encontrará fuera del arreglo
        j = i - 1
        # Mientras el valor de j sea mayor o igual a cero, y el arreglo en la posición j sea mayor al valor en la posición j
        while j >= 0 and arreglo[j] > val:
            # Arreglo se recorrerá una unidad(en el lugar de valor)
            arreglo[j+1] = arreglo[j]
            # Jota decrementa en una unidad
            j = j - 1
            # El valor que se encuentre en la nueva posicion de j sera el arreglo en j
            arreglo[j+1] = val


def Particionar(arreglo, low, high):
    # Se saca el valor del pibote, es decir el indice hight del arreglo
    x = arreglo[high]
    # Como no se sabe si hay numeros menores, ponemos el indice afuera
    i = low - 1
    # Se recorre con un for todo el arreglo, desde el inicio hasta el final
    for j in range(low, high):
        # Si el arreglo en la posicion j es menor al pibote, lo cambia
        if (arreglo[j] <= x):
            # Si no se hace el Swapeo da problemas, esto ayuda a que se eligan los valores para el cambio
            i = i + 1
            # Se hace un Swap que dice que a[i] se cambia por a[j] y que a[j] por a[i]
            # PYTHON HACE ESTO AUTOMATICAMENTE
            arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
    # Donde inicia mi parte de elementos más grandes, con el ultimo elemento, que es donde esta el piote
    arreglo[i+1], arreglo[high] = arreglo[high], arreglo[i+1]
    return i+1

# Aqui creamos la funcion quicsort que en sus parametros llevara la lista, el primer elemento del arreglo y el ultimo


def QuickSort(arreglo, iIni, iFin):
    if(iIni < iFin):
        iPiv = Particionar(arreglo, iIni, iFin)
        QuickSort(arreglo, iIni, iPiv-1)
        QuickSort(arreglo, iPiv+1, iFin)

######################################################


sys.setrecursionlimit(5000000)

# Creamos la lista que vamos a utilizar en el programa lista = [5, 3, 4, 1, 2, 7, 8, 6]
n = 5000
listaNormal = []
listaMejor = []
listaPeor = []

for i in range(n):
    listaNormal.append(random.randint(0, 10))

for i in range(n):
    listaMejor.append(i)

for i in range(n, 0, -1):
    listaPeor.append(i)

comparaciones = 0

normalA = []
normalB = []

mejorA = []
mejorB = []

peorA = []
peorB = []

#print ("LISTA NORMAL ES: ", listaNormal)
#print ("\n MEJOR LISTA ES: ", listaMejor)
#print ("\n PEOR LISTA ES: ", listaPeor)

normalA = listaNormal[:]  # Copiamos los valores de la listaNormal a normalA
t0 = time()
InsertionSort(normalA)
t1 = time()

#print ("\n QUICK SORT ORDENAMIENTO NORMAL: ", normalA)
print("\n Tiempo InsertionSort normal: {0:f} segundos".format(t1 - t0))
print("n: ", n, "\n")

normalB = listaNormal[:]
t0 = time()
QuickSort(normalB, 0,  len(normalB)-1)
t1 = time()
#print ("\n ORDENAMIENTO MERGE NORMAL: ", normalB)
print("\n Tiempo QUICK NORMAL: {0:f} segundos".format(t1 - t0))
print("\n n: ", n, "\n")

t0 = time()
mejorA = listaMejor[:]
InsertionSort(mejorA)
t1 = time()
#print ("\n BUBBLE ORDENAMIENTO MEJOR: ", mejorA)
print("\n Tiempo INSERTION mejor: {0:f} segundos".format(t1 - t0))
print("n: ", n, "\n")

mejorB = listaMejor[:]
t0 = time()
QuickSort(mejorB, 0,  len(mejorB)-1)
t1 = time()
#print ("\n ORDENAMIENTO MERGE MEJOR: ", mejorB)
print("\n Tiempo QUICK MEJOR: {0:f} segundos".format(t1 - t0))
print("\n n: ", n, "\n")

peorA = listaPeor[:]
t0 = time()
InsertionSort(peorA)
t1 = time()
#print ("\n BUBBLE ORDENAMIENTO PEOR: ", peorA)
print("\n Tiempo INSERTION PEOR: {0:f} segundos".format(t1 - t0))
print("n: ", n, "\n")

peorB = listaMejor[:]
t0 = time()
QuickSort(peorB, 0,  len(peorB)-1)
t1 = time()
#print ("\n ORDENAMIENTO MERGE PEOR: ", peorB)
print("\n Tiempo QUICK peor: {0:f} segundos".format(t1 - t0))
print("\n n: ", n, "\n")

#######################################################
