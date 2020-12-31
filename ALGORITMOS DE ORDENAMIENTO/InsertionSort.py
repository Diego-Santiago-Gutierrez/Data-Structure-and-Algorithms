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

A= [9, 0, 4, 6, 2, 1, 10]
print("Lista aleatoria: ", A)
InsertionSort(A)
print("Lista arreglada: ", A)