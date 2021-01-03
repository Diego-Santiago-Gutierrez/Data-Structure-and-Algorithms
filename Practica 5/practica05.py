import Database
from time import perf_counter
import sys
import random as rdn

#from Database import Usuario

usrList = Database.Usuario.GetUsuariosDB(600)
   
""""""""""""""""""

def creteTableHash(m): 
    HashTable = [ [] for _ in range(m) ]        #Creamos una tabla Hash con m elementos
    return HashTable                            #Estos elementos serán vacios []

tablaCreada=(creteTableHash(20))                 #CLAVE PRUEBA# AUN TENGO QUE AGREGAR ELEMENTOS UNU

""""""""""""""""""

def display_hash(tablaCreada):                  #Funcion que imprime la tabla en pantalla
      
    for i in range(len(tablaCreada)):           #Recorre el tamaño de la lista creada
        print(i, end = " ")                     #Imprime los lugares del arreglo 

        for j in tablaCreada[i]:                #Recorres tablaCreada en el indice i    
            print("-->", end = " ")       
            print(j, end = " ")                 #Muestra a j, que es el objeto 
              
        print()                                 #Lo imprime 

""""""""""""""""""

def Hashing(keyvalue):
    suma=0
    for item in keyvalue:
        suma = suma + ord(item)
        
    key = (( ( ( 49 * suma ) + 689 ) % 999983 ) % len((tablaCreada)))
    #print("KEY", key)
    #print("tamaño de la pendeja tabla", len(listaCreada))
    return key
    
""""""""""""""""""

def insert(tablaCreada, keyvalue, nameValue):       #Inserta los elementos dentro de la tabla Hashing 
                                                #Recibe la tabla creada, el valor de la llave para insertar y value es el dato que va insertar 
    
    hash_key = Hashing(keyvalue)                #La llave Hasheada 
    tablaCreada[hash_key].append(nameValue)         #Se inserta value en tablaCreada en el indice de hash_key 

""""""""""""""""""

def searchElement(tablaCreada, keyvalue):
    
    hash_key = Hashing(keyvalue)

    name = "" 
    for i in usrList: 
        if(keyvalue == i.username): 
            name = i.fullname
        else: 
            name = "Not matching found"

    for i in range (len(tablaCreada[hash_key])):
        if ( name in tablaCreada[hash_key][i] ):
            return tablaCreada[hash_key][i], True, name
        else: 
            return "", False, name
            
"""""""""""""""""" 
#Not match para cuando se sabe cuando niguno de los datos 
# dentro de la base de datos danot match porqe si 
# esta vacio quiere decir que cualquier elemetnoq ue 
# sea string dara verdaero en la evaluacion 

def login(tablaCreada, keyvalue, valuePasword):
    
    hash_key = Hashing(keyvalue)

    a = searchElement(tablaCreada, keyvalue)
    print("--------------------------------------------")
    print("LOGIN:   usr: " + keyvalue + "   pass: " + valuePasword)

    if (a[1]):
 
        #print("USUARIO EXISTE: ", a[0])
        for item in usrList: 
            if (valuePasword == item.password):
                return print("ACCESO AUTORIZADO bienvenido: ", a[2]) 
            else: 
                return print("ACCESO DENEGADO:  contraseña incorrecta",  a[2])      
    else:
        print("USUARIO NO EXISTE", a[2]) 

    print("--------------------------------------------")

"""""""""""""""""" 


for item in usrList:
    insert(tablaCreada, item.username, item.fullname)

#display_hash (tablaCreada) 

a = login(tablaCreada, 'mvicker23', 'TNqqef')
b = login(tablaCreada, 'tnewborn6x', 'FnZzio')
c = login(tablaCreada, 'tnewborn6x', '12313')
d = login(tablaCreada, 'Jesus Cruz', '12313')

print("-----------------------------------")             


t0 = perf_counter()
#d = login(tablaCreada, 'cchezier0', 'bXukce')
t1 = perf_counter()
print("\tTiempo busqueda: {0:f} segundos", (t1 - t0))
print("\t ", "\n")

def BusqLineal(userList, username): 
    for k in range (len(userList)):  
        if userList[k] == username:
            return k  
    return "No existe"

x = 0
y = 0
t1 = 0
t2 = 0
linealTime = 0
time = 0 

for x in range(10):

    n = rdn.randint(0,999)
    t1 = perf_counter()
    a = BusqLineal(tablaCreada, tablaCreada[n].username)
    t2 = perf_counter()

    linealTime = linealTime + (t2 - t1)

print("El promedio del tiempo de la busqueda lineal es:" , (linealTime / 10))


for y in range(10):
    n = rdn.randint(0,999)
    t1 = perf_counter()
    for item in usrList:
        a = searchElement( tablaCreada , tablaCreada[n].username)
    t2 = perf_counter()

    time = linealTime + (t2 - t1)

print("El tiempo promedio de la bsuqueda por Hash es de:" , (time / 10 ))
