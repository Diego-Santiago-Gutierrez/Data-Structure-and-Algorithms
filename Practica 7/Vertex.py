class Vertex: #Creamos la clase Vertex
    def __init__(self, name): #Constructor que recibe el nombre 
        self.name=name #Nombre 
        self.neighbors = [] #Vecinos 
        self.parentNode  = None #Padre de los nodos 
        self.color = "" #Color es el estado (Visitado, proceso, no visitado)
        self.distance = None #Distancia del nodo de un punto a otro 

    def __str__(self): #Metodos de impresion str
        return str(self.name)
    
    def __repr__(self): #Metodo de impresion repr objetos
        return str(self.name)
    
    def addNeighbor(self, nameVertex): #Creamos metodo que añade un nuevo vecino
                                   #vertex es el nombre 
        
        if nameVertex in self.neighbors: #Si ya existe el nodo, indica el vertice  
            print('Vecino ya existe', nameVertex.name , "En el vertice: " , self.name )
            return 
        
        self.neighbors.append(nameVertex) #Si no existe se incerta el vecino en la lista
        return 
