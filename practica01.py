#importamos la primera libreria para tomar el tiempo y otra para generar numeros aleatorios 
import random 
from time import time

# Creamos nuestra funcion que recibira un arreglo llamado "lista" 
def bubbleSort(lista):
    #Creamos una variable global para medir  comparaciones
    global comparaciones
    #n será el tamaño de la lista que nos ayudará a interar sobre sus incisos 
    n = len(lista)
    #Creamos una variable llamada intercambio para agilizar el progroama 
    intercambio = False
    #El for va del inicio al final de la lista 
    for i in range(1, n):
        #El for va del final al inicio 
        for j in range(n-i):
            #Se va agregando un contador de cuantas veces se realiza esto
            comparaciones += 1
            #Si la lista en J es mayor a una posicion adelante
            #cambian de lugar y el intercambio ha sido cierto 
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambio = True 
        #De lo contrario no devuelvas nada, se queda asi         
        if not intercambio:
            return 

#Creamos funcion que ira diviendo el programa 
def MergeSort(arr):
    n = len(arr)
    if n > 1:
        r = n // 2

        izq = arr[:r]
        der = arr[r:]

        MergeSort(izq)
        MergeSort(der)
        Merge(arr, izq, der)

#Creamos Merge que será quien acomode las listas, recibiendo izq y derecha 
def Merge(arr, izq, der):
    i = 0
    j = 0
    for k in range( len(arr) ):
        if( j >= len(der) ) or (i < len(izq) and izq[i] < der[j]):
            arr[k] = izq[i]
            i = i+1
        else:
            arr[k] = der[j]
            j = j+1

#######################################################

#Creamos la lista que vamos a utilizar en el programa lista = [5, 3, 4, 1, 2, 7, 8, 6] 
n = 10000
listaNormal = []
listaMejor = []
listaPeor = []

for i in range(n):
    listaNormal.append(random.randint(0, 10))

for i in range(n):
    listaMejor.append(i)

for i in range( n, 0, -1):
    listaPeor.append(i)

comparaciones = 0

mejorA = []
mejorB = []

peorA = []
peorB = []

normalA = [] 
normalB = []

#print ("LISTA NORMAL ES: ", listaNormal) 
#print ("\n MEJOR LISTA ES: ", listaMejor) 
#print ("\n PEOR LISTA ES: ", listaPeor) 


t0 = time()
normalA = listaNormal[:]
bubbleSort(normalA)
t1 = time()
#print ("\n BUBBLE ORDENAMIENTO NORMAL: ", normalA) 
print ("\n Tiempo BUBBLE NORMAL: {0:f} segundos".format(t1 - t0))
print ("\n Comparaciones:", comparaciones, "\n")
print ("n: ", n, "\n")

normalB = listaNormal[:]
t0 = time()
MergeSort(normalB)
t1 = time()
#print ("\n ORDENAMIENTO MERGE NORMAL: ", normalB)
print ("\n Tiempo MERGE NORMAL: {0:f} segundos".format(t1 - t0))
print ("\n Comparaciones:", comparaciones, "\n")
print ("\n n: ", n, "\n")

t0 = time()
mejorA = listaMejor[:]
bubbleSort(mejorA)
t1 = time()
#print ("\n BUBBLE ORDENAMIENTO MEJOR: ", mejorA) 
print ("\n Tiempo BUBBLE MEJOR: {0:f} segundos".format(t1 - t0))
print ("\n Comparaciones:", comparaciones, "\n")
print ("n: ", n, "\n")

mejorB = listaMejor[:]
t0 = time()
MergeSort(mejorB)
t1 = time()
#print ("\n ORDENAMIENTO MERGE MEJOR: ", mejorB)
print ("\n Tiempo MERGE MEJOR: {0:f} segundos".format(t1 - t0))
print ("\n Comparaciones:", comparaciones, "\n")
print ("\n n: ", n, "\n")

t0 = time()
peorA = listaPeor[:]
bubbleSort(peorA)
t1 = time()
#print ("\n BUBBLE ORDENAMIENTO PEOR: ", peorA) 
print ("\n Tiempo BUBBLE PEOR: {0:f} segundos".format(t1 - t0))
print ("\n Comparaciones:", comparaciones, "\n")
print ("n: ", n, "\n")

peorB = listaMejor[:]
t0 = time()
MergeSort(peorB)
t1 = time()
#print ("\n ORDENAMIENTO MERGE PEOR: ", peorB)
print ("\n Tiempo MERGE PEOR: {0:f} segundos".format(t1 - t0))
print ("\n Comparaciones:", comparaciones, "\n")
print ("\n n: ", n, "\n")

#######################################################

