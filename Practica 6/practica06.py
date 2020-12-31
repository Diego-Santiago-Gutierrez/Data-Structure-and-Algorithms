import sys 

class Vertex: 

    def __init__(self, name):
        #Atributos de la clase Vertex 
        self.name=name
        self.neighbors = []
        self.parentNode  = None
        self.color = ""
        self.distance = 0 

    def __str__(self): 
        return self.name
    
    def __repr__(self):
        return self.name

    #Creamos metodo que añade un nuevo vecino 
    def addNeighbor(self, vertex): 
        #Si ya existe vertex en vecinos, indica posicion
        if vertex in self.neighbors:  
            print('Vecino ya existe', vertex.name , "En el vertice: " , self.name )
            return 
        #Si no existe se incerta en vecinos el vertice    
        self.neighbors.append(vertex)



#Creamos la clase Grafo
class Grafo: 
    #Atributos de la clase
    def __init__(self):
        self.vertexs = {}

    def __str__(self):
        cadena = ''
        for nameVertex in self.vertexs:
            cadena = cadena+nameVertex + "->" + str(self.vertexs[nameVertex].neighbors)+"\n"
        return cadena
    
    def __repr__(self): 
        return self.vertexs

    #Metodo que permite la adicion de un vertice
    def addVertex(self, nameVertex):
        #Verifica si el vertice ya existe en el diccionario de vertices 
        if nameVertex in self.vertexs: 
            print('Ya existe: ', nameVertex)
            return False 
        #Si no se cumple el if, añade el vertice en el ojeto 
        vertex = Vertex(nameVertex)
        self.vertexs[nameVertex] = vertex 
        return True

    #Metodo que añade arista 
    def addBranch(self, nameVertex1, nameVertex2):
        #Si el vertice uno no está en vertexs
        if not nameVertex1 in self.vertexs:
            print('Error al agregar arista. No existe le vertice 1', nameVertex1)
            return False
        #Si el vertice dos no se encuentra el nombre del vertice2 en vertex
        if not nameVertex2 in self.vertexs:
            print('Error al agregar arista. No existe el vertice 2', nameVertex2)
            return False
        #Basicamente no pudes agregar algo que no existe 
        #añadimos estos dos nuevos vertices 
        vertex1 = self.vertexs[nameVertex2]
        vertex2 = self.vertexs[nameVertex1]

        vertex1.addNeighbor(vertex2)
        vertex2.addNeighbor(vertex1)

        #¿Que modificaciones hay que hacer si es un grafo dirigido 

        return True 

    
def EjemploBasico():
    
    g = Grafo()  

    g.addVertex("0")
    g.addVertex("1")
    g.addVertex("2")
    g.addVertex('3')
    g.addVertex('4')
    g.addVertex('5')
    g.addVertex('6')
    g.addVertex('7')

    #Que pasa si se agreaga un ariste en un vertice que no existe ? 
    if True: 
        
        g.addBranch('0', 'asdasdasd')

    g.addBranch('0', '1')
    g.addBranch('0', '2')
    g.addBranch('0', '3')

    #Que pasa si se agrega un arista que ya existe ? 
    if True: 
        g.addBranch('1', '0')
    
    g.addBranch('1', '2')
    g.addBranch('2', '3')
    g.addBranch('3', '4')
    g.addBranch('4', '5')
    g.addBranch('4', '6')
    g.addBranch('5', '6')

    print('####Grafo####')
    print(g)

    actualNode = g.vertexs["0"]; 
    while( actualNode != None ):
        print(actualNode.name , '->')
        actualNode = actualNode.parentNode 

if __name__ == "__main__":
    EjemploBasico() 
