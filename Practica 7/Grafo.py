from Vertex import Vertex #Exportamos el Vertex 

class Grafo: #Creamos la clase Grafo
    def __init__(self): #Atributos de la clase
        self.vertexs = {} #Diccionario llamado vertices

    def __str__(self): #Metdo para imprimir como cadena los nodos
        cadena = ''
        for nameVertex in self.vertexs:
            cadena = cadena+nameVertex + "->" + str(self.vertexs[nameVertex].neighbors)+"\n"
        return cadena
    
    def __repr__(self): #Metodo para imprimir objetos de los nodos
        return self.vertexs

    
    def addVertex(self, nameVertex): #Metodo que añade un nodo 
        if nameVertex in self.vertexs: #Verifica si el vertice ya existe en el diccionario de vertices 
            print('Ya existe: ', nameVertex)
            return False 
        
        self.vertexs[nameVertex] = Vertex(nameVertex) 
        #Si no se cumple el if, se crea un vertex 
        #tipo Vertex que recive el nombre del nodo 
        #Crea una key con nameVertex y un value tipo Vertex con su nombre
        #{nameVertex: Vertex} 
        return

    def addBranch(self, nameVertex1, nameVertex2):#Metodo que añade arista
        
        if not nameVertex1 in self.vertexs: #Si no existe el nodo 1
            print('Error al agregar arista. No existe le vertice 1', nameVertex1)
            return False
        
        if not nameVertex2 in self.vertexs: #Si no existe el nodo 2
            print('Error al agregar arista. No existe el vertice 2', nameVertex2)
            return False

        self.vertexs[nameVertex1].addNeighbor(self.vertexs[nameVertex2]) #A es vecino de B
        self.vertexs[nameVertex2].addNeighbor(self.vertexs[nameVertex1]) #B es vecino de A
        return

    def BFS (self, nameFirstNodo): #Metodo BFS que recibe un nodo para buscar
        for u in self.vertexs.values(): #Reseteamos todo el nodo, nuevecito queda
            u.color = "blanco"
            u.distance = None
            u.parentNode = None;
        
        if nameFirstNodo not in self.vertexs.keys(): #Verificamos si el nodo existe con su key del diccionario
            print("El nodo no es parte del arreglo") #Si no existe le do decimos 
            return
        
        nodeInitial = self.vertexs[nameFirstNodo] #Key->NameFirstNode , value->nodeInitial
        nodeInitial.color = "gris" #Marcamos como en proceso
        nodeInitial.distance  = 0 #La distancia del primer nodo es 0

        q = list() #Creamos una lista que será utilizada como cola 
        q.append(nodeInitial) #Insertamos en la cola el nodoInicial

        while (len(q) > 0): #Mientras este lleno la lista
            actualNode = q.pop(0) #Se saca el inicial, dando comportamiento de cola
            #actualNode = u 
            #explorerNode = v 
            for v in actualNode.neighbors: #Actual nodo es el primer elemento de la cola 
                                           #Buscamos en sus vecinos
                                            
                if v.color == "blanco": #Si nodo vecino no ha sido explorado
                    v.color = "gris" #Ya que ha sido explorado ahora es gris 
                    v.distance = actualNode.distance + 1 #Su distancia es uno mas que el padre
                    v.parentNode = actualNode.name #Su padre será el nombre del nodo actual

                    q.append(v)  #Insertamos a v en la cola
            
            self.vertexs[actualNode.name].color = "negro" #Volvemos negro el nodo una vez que haya sido explorado
  
    def RutaBFS(self, InitialNode, FinalNode): #Para conocer la ruta necesitamos de donde empezar 
                                               #Y donde terminar

        self.BFS(InitialNode) #Hacemos BFC con el nodo inicial 
        lines = list() #Creamos una lista 
        actualNode = self.vertexs[FinalNode] #Nodo actual será el final de la busqueda

        while True:
            lines.append(actualNode.name) #Incertaremos en la lista el nombre del nodo
            if actualNode.parentNode == None: #Si llegamos None (sin hijos ya)
                break #Salimos
            actualNode = self.vertexs[actualNode.parentNode] #Pasamos al nodo padre de este
            #{padre: actualNode}

        print("------------------R U T A - B F S------------------------------")
        print("\tPARADA: ", InitialNode, "\tDESTINO: ", FinalNode)
        print("\t\tTOTAL DE ESTACIONES: ", len(lines) )

        cadena = lines[len(lines)-1]
        for i in range(len(lines)-1, -1, -1):
            cadena += "-->" + lines[i]
        print("MOSTRANDO RUTA: ", cadena )

    def DFS (self, nameFirstNodo): #Metodo de busqueda DFS
        for u in self.vertexs.values(): #Reseteamos todos los valores del diccionario
            u.color= "blanco"
            u.parentNode = None
            u.distance = None

        if nameFirstNodo not in self.vertexs.keys(): #Si no se encuentra el nombre en el diccionario
            print("No esta en el arreglo") 
            return

        actualNode = self.vertexs[nameFirstNodo] #El nodo actual será el que estemos buscando
        actualNode.color = "gris" #Como sabemos que estamos ahí, lo volvemos gris
        actualNode.distance = 0  #Su distancia es 0 por ser el inicial
        self.DFSearch(actualNode) #Buscamos el camino con una función aparte

    def DFSearch(self, actualNode):
    
        for v in actualNode.neighbors:  #Recorremos en los vecinos del nodo actual
            if v.color == "blanco": #Si no han sido explorados 
                v.parentNode = actualNode.name #El primer nodo vecino será el nombre del actual
                v.color = "gris" #Su color será gris ya que estando en el se explora
                v.distance = actualNode.distance + 1 #La distnacia será la del nodo actual más uno
                self.DFSearch(v) #Buscamos en el primer vecino del vecino de ahorita hasta que ya no haya mas
        
        actualNode.color= "negro" #El nodo actual se vuelve negro una vez acabando de explorar
        return 

    def RutaDFS(self, InitialNode, FinalNode ): #Buscamos la ruta inicial a un punto final

        self.DFS(InitialNode) #LBuscamos con DFS el camino del nodo inicial
        lines = list()  #Creamos una lista que será usada como pila
        ActualNode = self.vertexs[FinalNode] #El nodo punto final será nuestro nodo actual

        while True: #Mientras haya elementos que incertar
            lines.append(ActualNode.name) #Incertamos el nodoACtual(final)
            if ActualNode.parentNode == None: #Si se llega al padre que apunta a null, salimos
                break
            ActualNode = self.vertexs[ActualNode.parentNode] #Hasta entonces buscaremos en el padre del padre del padre
            #{ActualNode.parentNode : actualNode}
        print("------------------R U T A - D F S------------------------------")
        print("\tPARADA: ", InitialNode, "\tDESTINO: ", FinalNode)
        print("\t\tTOTAL DE ESTACIONES: ", len(lines) )

        cadena = lines[len(lines)-1]
        for i in range(len(lines)-1, -1, -1):
            cadena += "-->" + lines[i]
        print("MOSTRANDO RUTA: ", cadena )

        