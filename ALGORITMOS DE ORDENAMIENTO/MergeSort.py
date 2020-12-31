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
        if( j >= len(der) ) or (i < len(izq) and izq[i] < der[j]): #Si se llega a salir en i entonces el ultimo elemento de j va en la posicion k
            arr[k] = izq[i] #El lado izquiedo es menor
            i = i+1
        else:
            arr[k] = der[j] #El lado derecho es el pequeño
            j = j+1

A= [9, 0, 4, 6, 2, 1, 10]
print("Lista aleatoria: ", A)
MergeSort(A)
print("Lista arreglada: ", A)