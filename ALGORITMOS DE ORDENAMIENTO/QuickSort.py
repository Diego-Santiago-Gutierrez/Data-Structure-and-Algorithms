def Particionar (array, low, high):
    pivot = array[high]
    i = low-1 
    for j in range(low, high):
        if ( array[j] <= pivot ):
            i= i+ 1 
            array[i], array[j] = array[j], array[i] #Swap
        
    array[i+1], array[high] = array[high], array[i+1]

    return i+1

def QuickSort(arr, iIni, iFin):
    if( iIni < iFin ): #Si hay elementos 
        iPiv=Particionar(arr, iIni, iFin)
        QuickSort(arr, iIni, iPiv-1) #Direccion del arreglo, por eso cambia en ejecucion 
        QuickSort(arr, iPiv+1, iFin)


A= [9, 0, 4, 6, 2, 1, 10]
print("Lista aleatoria: ", A)
QuickSort(A, 0 , len(A)-1)
print("Lista arreglada: ", A)