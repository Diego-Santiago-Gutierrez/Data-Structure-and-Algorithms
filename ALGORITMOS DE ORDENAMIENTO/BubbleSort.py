# Creamos nuestra funcion que recibira un arreglo llamado "lista" 
def bubbleSort(lista):
    #Creamos una variable global para medir  comparaciones
    #n será el tamaño de la lista que nos ayudará a interar sobre sus incisos 
    n = len(lista)
    #Creamos una variable llamada intercambio para agilizar el progroama 
    intercambio = False
    #El for va del inicio al final de la lista 
    for i in range(1, n):
        #El for va del final al inicio 
        for j in range(n-i):
            #Si la lista en J es mayor a una posicion adelante
            #cambian de lugar y el intercambio ha sido cierto 
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambio = True 
        #De lo contrario no devuelvas nada, se queda asi         
        if not intercambio:
            return 


A= [9, 0, 4, 6, 2, 1, 10]
print("Lista aleatoria: ", A)
bubbleSort(A)
print("Lista arreglada: ", A)
