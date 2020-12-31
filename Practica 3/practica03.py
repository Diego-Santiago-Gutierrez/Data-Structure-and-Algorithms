#IMPORTAMOS LAS LIBRERIAS A USAR
import random
import math
from time import time
import sys

#DEFINIMOS NUESTRA FUNCION LLAMADA CountingSort que recibirá un arreeglo:
def CountingSort(A):    
    n = len(A) #n es del tamaño del arreglo
    k = max(A) #k es el valor más alto del arreglo
    C = [0]*(k+1) #Una unidad más que el valor maximo sera el numero de elementos que serán rellenados con 0
    B = [0]*(n) #Una lista llena de 0 que tenga el tamaño del arreglo que estaremos trabajando 

    for j in range(n): #For de j al tamaño del arreglo(Para ir llenando)
        C[A[j]] += 1 #El arreglo de C (que es el que tiene una unidad mas que k) en la posicion 0 del arreglo A se incrementará e6n uno si el elemento 
                     #El numero en la posicion de j de A será el numero que guardará registro de su existencia en la posicion del arreglo
                     #Es decir, si A[0]=3, entonces C[3]= 1 y este for iterará hasta que se acabe el arreglo 

    for j in range(1, k+1): #for de j a el valor maximo mas uno, es decir si el valor maximo es 15, el ciclo irá de 1 a 16
        C[j] += C[j-1] #C[j] su valor se sumara con la posición anteior y se asigará a la posicion de C[j]

    for j in range(n-1,-1,-1): #For ira del tamaño del arreglo hasta -1 e irra decrementando en uno
        B[C[A[j]]-1] = A[j] #Con en arrelgo B que es el que tiene el tamaño del arreglo A 
                            #Buscaremos el valor que hay en el inciso a[j] y se le restará una unidad, ejemplo si en su valor es A[j] = 1 -> A[j] = 0
                            #Con el numero del arreglo anterior, se buscará en el indice del arreglo de C[0] siguiendo el ejemplo de arriba 
                            #Para que el valor que este en C[0] sea el idice del arreglo B y posterior a eso se tendrá que asignarle el valor de A[j] que era uno (Todo siguiendo ejemplos)
        
        C[A[j]] -= 1 #Para esto se le resta el valor del contador que llevamos para dar a entender que ese elemnto ha sido acomodado
    return B #Regresa el arreglo ordenado

def RadixSort(A): #Creamos nuestra funcion llamada RadixSort que recibe un arreglo 
    k = max(A) #Sacamos el valor maximo del arreglo 
    d = (int)(math.log10(k)+1) #Creamos d que por medio de una libreria sacamos el valor logaritmico en base diez del valor mas alto del arreglo 
    for i in range (d):# Veces que tendremos que hacer este proceso del calculo del logaritmo del valor más alto del arreglo  
        A = CountingSort2(A,i) #El arreglo sera recursivo y lo que tengamos en A lo iremos procesando con CountingSort2 
    return A #Retornamos el valor del arreglo ya cuando acabe el arreglo 

def CountingSort2(A,i): #Declaramos nuestra funcion que recibirá un arreglo y le pasas el indice del arreglo de Radix 
    n = len(A) #Sacas el tamaño del arreglo en A 
    k = 9 
    C = [0]*(k+1) # llenamos el k+1 espacios de un arreglo con 0
    B = [0]*(len(A)) #Creamos y lleanamos el arreglo B con el tamaño del arreglo A con puros 0

    for j in range(n): #For del tamaño de i hasta el tamaño del arreglo a usar 
        val = A[j] #Val se le asigna el valor del arreglo en la posicion j 
        di = (val // 10**i) % 10 #di nos ayuda a encontrar el modulo del valor mas pequeño de todos los valores, obteniendo la unidad de los numeros que tengamos 
        C[di] += 1 #C ira almacenando y recorriendo para poder hacer este proceso  
    
    for j in range(1, k+1): #j en el rango de (1 a k+1)
        C[j] += C[j-1] #La posicion en C[j] se sumará al valor que este dentro de la posicion c(j-1) para asignarlo al mismo C[j]
    
    for j in range(n-1,-1,-1): #Ira del tamaño del arreglo hasta -1, es decir que no haya elemetnos y este ira recorriendo de menos uno en menos uno 
        val = A[j] #val se le asignará el valor de lo que tenga la poscicion A[j] 
        di = (val // 10**i) % 10 #Sacamos el valo de la unidad para ir comparando con los valores 
        B[C[di]-1] = val #El valor del arrego C[di] menos uno, sera el indice para el arreglo de B para poder guardarlo en val
        C[di] -= 1 #Retiramos un
    return B # regresamos el arreglo ya ordenado de A 

######################################################


sys.setrecursionlimit(5000000)

# Creamos la lista que vamos a utilizar en el programa lista = [5, 3, 4, 1, 2, 7, 8, 6]
n = 10000
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

#print ("\n RadixSort ORDENAMIENTO NORMAL: ", normalA)
normalA = listaNormal[:]  # Copiamos los valores de la listaNormal a normalA
t0 = time()
RadixSort(normalA)
t1 = time()
print("\n Tiempo RadixSort normal: {0:f} segundos".format(t1 - t0))
print("n: ", n, "\n")

#print ("\n RadixSort ORDENAMIENTO MEJOR: ", normalA)
mejorA = listaMejor[:]  # Copiamos los valores de la listaNormal a normalA
t0 = time()
RadixSort(mejorA)
t1 = time()
print("\n Tiempo RadixSort MEJOR: {0:f} segundos".format(t1 - t0))
print("n: ", n, "\n")

#print ("\n RadixSort ORDENAMIENTO PEOR: ", normalA)
peorA = listaPeor[:]  # Copiamos los valores de la listaNormal a normalA
t0 = time()
RadixSort(peorA)
t1 = time()
print("\n Tiempo RadixSort PEOR: {0:f} segundos".format(t1 - t0))
print("n: ", n, "\n")

#print ("\n ORDENAMIENTO CountingSort NORMAL: ", normalB)
normalB = listaNormal[:]
t0 = time()
CountingSort(normalB)
t1 = time()
print("\n Tiempo CountingSort NORMAL: {0:f} segundos".format(t1 - t0))
print("\n n: ", n, "\n")

#print ("\n ORDENAMIENTO CountingSort MEJOR: ", normalB)
mejorB = listaMejor[:]
t0 = time()
CountingSort(mejorB)
t1 = time()
print("\n Tiempo CountingSort MEJOR: {0:f} segundos".format(t1 - t0))
print("\n n: ", n, "\n")

#print ("\n ORDENAMIENTO CountingSort PEOR: ", normalB)
peorB = listaPeor[:]
t0 = time()
CountingSort(peorB)
t1 = time()
print("\n Tiempo CountingSort PEOR: {0:f} segundos".format(t1 - t0))
print("\n n: ", n, "\n")

#######################################################
