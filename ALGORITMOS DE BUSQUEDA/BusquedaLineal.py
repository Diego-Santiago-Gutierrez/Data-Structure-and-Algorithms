def BusqLineal(A, x): #Recibe un arrleglo A y X que es el elemento a buscar 
    for k in (A): #Recorremos el arreglo A para ir realizando la busqueda
        if A[k] == x: #If A en la posicion k es igual a X
            return k #Te regresara K que es la posicion del arreglo 
    return "No existe" #Si no se encontró nada regresa un none 

d=[3, 5, 22, 40,42, 43, 45, 47, 55]
a=BusqLineal(d, 40)
print("Número encontrado en el indice: ",a)
