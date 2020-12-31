from queue import Queue
from  typing import Optional
from Nodee import Node

        
class  BinaryTree():

    def __init__(self):                  #Contructor de la clase
        self.root: Optional[Node] = None #Atributo que espera recibir nodos

    def addRoot(self, value: int):           #Metodo agregar
        if self.root is None:                #Si la raiz esta vacia 
            self.root = Node(value)          #el primer valor será la raiz
            return

        parentNode = self.root               #El nodo padre será la raíz 
        if parentNode.value == value:        #Si el valor del padre es igual a un valor ya existente
            raise KeyError("Valor repetido") #Arroja una excepcion 
        
        if value < parentNode.value:            #Si es menor 
             childNode = parentNode.leftChild   #va del lado izquierdo
        else:                                   #Entonces
            childNode = parentNode.rightChild   #Es mayor

        while childNode != None:                 #Mientras el nodo hijo tenga valores
            parentNode = childNode               #El nodopadre será el nodo hijo 
            
            if parentNode.value == value:        #Si el valor del nodo padre es igual al nodo que se quiere agregar
                raise KeyError("Valor repetido") #Lanzará una excepcion
            
            if value < childNode.value:          #Si es menor el nodo izq del hijo
                childNode = childNode.leftChild  #Entonces se guarda en el lado izquiedo
            else:                                #De lo contrario
                childNode = childNode.rightChild #Es el nodo derecho el hijo 

        newNode = Node(value)                    #Tendremos un nuevo nodo tipo Node 
        newNode.parentNode = parentNode          #El padre del nuevo nodo será el padre actual

        if newNode.value < parentNode.value:     #Si el valor del nuevo nodo es menor al valor del nodo padre
            parentNode.leftChild = newNode       #Lo guardamos en el lado izquiedo del nodo el nuevo nodo 
        else:
            parentNode.rightChild = newNode      #Sino lo guardamos del lado derecho al nuevo nodo

    def _AddNode(self, value , node):                   #Metodo para agregar un nodo
        if ( value < node.value ):                      #Si el valor es menor al nodo 
            if( node.leftChild != None ):               #Si el nodo  ya existe
                self._AddNode( value, node.leftChild )  #Lo agregamos
            else:
                
                node.leftChild = Node(value)            #Si no hay, este será el nodo
        
        else:                                           #Si el valor es mayor
            if( node.rightChild !=None ):               #Si el nodo izquierdo del hijo tiene valores
                self._AddNode(value, node.rightChild )  #Lo agregamos al nodo derecho 
            else:                                       #si no hay nodo de lado derecho 
                node.rightChild = Node( value )         #solo se agregar el nodo con nuestro valor

    def _Search( self, node: Node , value: int ):       #Busqueda de un valor
        if (node == None or node.value == value):       #Verificamos que tenga valor
            return node                                 #Regresamos este nodo

        elif value < node.value:                        #Si el valor es menor al valor del nodo
            return self._Search(node.leftChild, value)  #Se busca del lado izquierdo 
        else:
            return self._Search(node.rightChild, value) #Si es mayor, del lado derecho      

    def Min(self, node: Node = None):          #Valor minimo
        if node == None:                       #Si el nodo esá vacio 
            if self.root == None:              #Si la raiz esta vacia 
                return None                    #Regresa un None
            node = self.root                   #Si solo el nodo es None pero hay raiz 
                                               #El nodo es la raiz

        while node.leftChild != None:          #Mientras que el nodo hijo izquierdo tiene valores
            node = node.leftChild              #El nodo ahora será el nodo izquiedo del mismo
        return node                            #Regresamos este nodo cuando acabe el while 

    def Max(self, node: Node = None):          #Valor maximo
        if node == None:                       #Si el nodo está vacio
            if self.root == None:              #Si la raiz esta vacia
                return None                    #Entonces no hay nada
            node = self.root                   #Si hay nodo pero no raiz, entonce el nodo es la raiz

        while node.rightChild != None:         #Mientras el nodo hijo derecho tenga valores
            node = node.rightChild             #El nodo actual será el nodo derecho
        return node                            #Hasta que llegue a null y regrese ese valor

    def Delete( self, value: int):                #Borrar valor 
        valueDelete = self._SearchHelper( value ) #Con una funcion se desea eliminar
        if valueDelete != None:                   #Si el valor existe
            self._HelperDelete(valueDelete)       #Se busca apartir del valor a eliminar
        else:
            print("No existe valor en el arbol")  #Si no se encuentra, no se puede eliminar

    def _SearchHelper(self, value: int):          #Buscador ayuda
        return self._Search(self.root , value)    #Busca en el arbol el valor

    def NextNode( self, node: Node):        #Metodo para saber el nodo siguiente
        if node == None:                    #si no hay nodo
            return None                     #Regresa un nodo

        if node.rightChild != None:            #Si el nodo hijo derecho existe
            return self.Min( node.rightChild ) #Se busca el minimo de este nodo 

        aux = node.parentNode                  #Creamos una variable auxiliar que sea el nodo padre
        auxChild = node                        #El nodo hijo es el nodo actual

        while aux != None:    #mientras la variable auxiliar no sea none
            auxChild = aux    #El hijo auxiliar tomará el valor de la auxiliar
            aux = aux.parentNode #y aux ahora será el nodo padre de este

        return aux              #Regresa el valor auxiliar que ahora era el padre del auxiliar
    
    def PreviousNode( self, node: Node ):   #Metodo para saber el nodo anterior

        if node == None:                    #Si el nodo no tiene valor
            return None                     #Regresa un none
    
        if node.leftChild == None:          #Si el nodo izquiedo hijo esta vacio
            return self.Max( node.leftChild ) #Regresa el valor maximo de este (el mismo)

        aux = node.parentNode                 #Creamos una variable auxiliar del nodo padre
        auxChild = node                       #El hijo ahora es el padre

        while aux != None:                    #Si el axuliar tiene valoress
            auxChild = aux                    #El hijo es guardado en una variable auxiliar
            aux = aux.parentNode              #El auxiliar del padre sera el nuevo auxiliar

        return aux                            #Regresa el valor auxiliar

    def _reTransplant ( self , original: Node , reemplazo: Optional[ Node ]): 

        if original.parentNode == None:                 #Si el padre del nodo que buscamos remplazar esta vacio 
            self.root = reemplazo                       #La raiz será el valor a remplazar
        elif original == original.parentNode.leftChild: #O si el valor original es igual al hijo izquiedo del padre del nodo
            original.parentNode.leftChild = reemplazo   #este será el valor a remplazar por el hijo izquierdo 
        else:
            original.parentNode.rightChild = reemplazo  #De lo contrario se remplaazara del lado derecho
        
        if reemplazo != None:                           #Si el remplazo es diferente de none 
            reemplazo.parentNode = original.parentNode  #EL padre del demplazo será el nodo original que teniamos 
    
    def _HelperDelete( self, node: Node):                   #Ayuda a elmininar 
                                                            
        if node.leftChild == None:                          #si el nodo izquierdo es vacio
            self._reTransplant ( node, node.rightChild )    #Se replanta el arbol del valor derecho
        elif node.rightChild == None:                        #Si el nodo derecho esta vacio
            self._reTransplant ( node, node.leftChild )      #Se replanta del valor izquiedo
        else:
            nextNode = self.Min(node.rightChild)             #el nodo siquiente será el valor de este, buscado por izq
            if nextNode.parentNode != node:                  #Si el padre del nodo siguiente es diferente al nodo
                self._reTransplant ( nextNode, nextNode.rightChild )    #Se resplanta al nodo siquiente por el valor del hijo derecho
                nextNode.rightChild = node.rightChild           #El nodo siguiente hijo es ahora e nodo derecho hijo 
                nextNode.rightChild.parentNode = nextNode       #el padre del nodo derecho del nodo actual será el nodo siguente

    def Print(self):                                        #metodo imprimir
        if self.root == None:
            return print("El arbol actual esta vacio \n")
        else:
            preOrder = self.__valuesList(self.__preorder)
            inOrder = self.__valuesList(self.__inorder)
            postOrder = self.__valuesList(self.__postorder)
            anchura = self.__valuesList(self.__anchura_traversal)
            print("Preorder:", preOrder)
            print("Inorder:", inOrder)
            print("Postorder:", postOrder)
            print("Anchura:", anchura, "\n")
            self.__printPretty()
            print()
    
    def __valuesList(self, traversalAlg):  #Lista de los nodos 
        return traversalAlg(self.root)

    def __inorder(self, root: Node):       #InOrden(izq) – Raiz – InOrden(Der)
        if root == None:
            return ""
        base = self.__inorder(root.leftChild)
        base += " -> " + str(root.value)
        return base + self.__inorder(root.rightChild)

    def __preorder(self, root: Node):       #RAIZ-PREORDEN(IZQ)-PREORDEN(DER) 
        if root is None:
            return ""
        base = " -> " + str(root.value)
        base += self.__preorder(root.leftChild)
        return base + self.__preorder(root.rightChild)

    def __postorder(self, root: Node):      #PostOrden(izq) – PostOrden(Der) – Raiz
        if root is None:
            return ""
        base = self.__postorder(root.leftChild)
        base += self.__postorder(root.rightChild)
        return base + " -> " + str(root.value)

    def __anchura_traversal(self, root: Node): #BFS
        if root is None:
            return ""

        queue = Queue()
        base = ""
        queue.put(self.root)

        while not queue.empty():
            current = queue.get()
            base += " -> " + str(current.value)

            if current.leftChild != None:
                queue.put(current.leftChild)

            if current.rightChild != None:
                queue.put(current.rightChild)

        return base

    def __getDepth(self): #Metodo que obtiene la profundidad del arbol
        if self.root == None:
            return 0

        queue = Queue()     #Creamos una cola tipo cola
        queue.put(self.root)   #Insertamos la raiz 
        depth = 0       #la profundidad de esto es cero

        while not queue.empty(): #Mientras la cola no este vacia 
            size = queue.qsize() #Se tomará el valor de la cola 
            depth += 1 #su profndidad será cada vez mayor hasta estar vacia 

            for _ in range(size):               #Se recorre el tamaño
                value = queue.get()           #Obtenemos el valor de la cola 
                if value.leftChild != None:     #Y buscamos del lado del hijo izquiedo
                    queue.put(value.leftChild)  #Insertando su valor
                if value.rightChild != None:    #Lo mismo con el hijo derecho 
                    queue.put(value.rightChild)

        return depth - 1

    def __printPretty(self): #Metodo para imprimir bonito
        if self.root is None:  #si la raiz no tiene valores 
            return                 #salimos
        maxDepth = self.__getDepth() #Buscamos la altura maxima 
        largestLineLength = 2 ** (maxDepth + 2) - 3 
        TOTAL_LINES = maxDepth + 1
        TOTAL_EDGE_LINES = 2**(maxDepth + 1) - 1 - maxDepth
        nodesLines = [[" "] * largestLineLength for _ in range(TOTAL_LINES)]
        edgesLines = [[" "] * largestLineLength for _ in range(TOTAL_EDGE_LINES)]

        def __drawEdge(depth: int, position: int, idxMutator, edge: str): #Dibujar aristas

            finalDepth = int(2**(maxDepth + 1) * (-0.5**depth + 1) - depth)
            startDepth = finalDepth - 2**(maxDepth-depth+1) + 2
            currentCharIdx = position
            for currDepth in range(startDepth, finalDepth+1):
                currentCharIdx = idxMutator(currentCharIdx)
                edgesLines[currDepth][currentCharIdx] = edge

        def __drawEdgeLeft(depth: int, position: int): #Aristas izquiedas
            def indexMutator(idx: int):
                return idx - 1
            __drawEdge(depth, position, indexMutator, "/")

        def __drawEdgeRight(depth: int, position: int): #Aristas Derechas 
            def indexMutator(idx: int):
                return idx + 1
            __drawEdge(depth, position, indexMutator, "\\")

        def __miniTree(root: Node, depth: int, position: int): #Dibujamos las lineas de los arboles pequeños
            nodesLines[depth][position] = str(root.value)

            if root.leftChild is not None:                      #Si no esta vacio lo dibuja
                __drawEdgeLeft(depth + 1, position)
                __miniTree(root.leftChild, depth + 1, position - 2**(maxDepth - depth))

            if root.rightChild is not None:                     #si no esta vacio lo dibuja 
                __drawEdgeRight(depth + 1, position)
                __miniTree(root.rightChild, depth + 1, position + 2**(maxDepth - depth))

        __miniTree(self.root, 0, largestLineLength // 2)    #Estableemos el patron de dibujo 
        print("".join(nodesLines[0]))
        i = 1
        for currentDepth in range(1, maxDepth+1):           #insertamos lineas 
            for _ in range(2**(maxDepth - currentDepth + 1) - 1):
                print("".join(edgesLines[i]))
                i += 1                                      

            print("".join(nodesLines[currentDepth]))        #imprimimos linea
     