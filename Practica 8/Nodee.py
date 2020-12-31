class Node:#Clase Node
    def __init__(self , value: int):#Atributos de la clase

        self.value:int = value
        self.parentNode: Optional[Node] = None
        self.leftChild: Optional[Node] = None
        self.rightChild: Optional[Node] = None