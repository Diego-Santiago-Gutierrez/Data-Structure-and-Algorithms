from BinaryTree import BinaryTree 
def main():
    arbol = BinaryTree()
    arbol.Print()
    arbol.addRoot(8)
    arbol.addRoot(3)
    arbol.addRoot(10)
    arbol.addRoot(1)
    arbol.addRoot(6)
    arbol.addRoot(14)
    arbol.addRoot(4)
    arbol.addRoot(7)
    arbol.addRoot(13)
    arbol.Print()
    try:
        arbol.addRoot(14)  # Repetido, debe mostrar mensaje de error
    except KeyError:
        print("El nodo con llave 14 ya se encuentra en el árbol")
    try:
        arbol.addRoot(1)  # Repetido, debe mostrar mensaje de error
    except KeyError:
        print("El nodo con llave 1 ya se encuentra en el árbol")
    print("Mínimo:", arbol.Min().value)
    print("Máximo:", arbol.Max().value)
    arbol._SearchHelper(4)
    arbol._SearchHelper(8)
    arbol._SearchHelper(13)
    arbol._SearchHelper(2)
    arbol._SearchHelper(15)
    arbol.Delete(7)  # Borrando el 7 (sin hijos)
    arbol.Print()
    arbol.Delete(10)  # Borrando el 10 (solo hijo der)
    arbol.Print()
    arbol.Delete(6)  # Borrando el 6 (solo hijo izq)
    arbol.Print()
    arbol.Delete(3)  # Borrando el 3 (ambos hijos)
    arbol.Print()
    try:
        arbol.Delete(3)  # Borrando el 3 (nodo no existe)
    except KeyError:
        print("El nodo con llave 3 no se encuentra en el árbol")
    arbol.Print()
    arbol.Delete(8)  # Borrando el 8 (raíz, ambos hijos)
    arbol.Print()
    arbol.addRoot(100)
    arbol.Print()           


main()
