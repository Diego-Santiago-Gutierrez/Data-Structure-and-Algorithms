import Database
from time import perf_counter
import sys
import random as rdn
import random
import time
#from Database import Usuario

usrList = Database.Usuario.GetUsuariosDB(1000)
   
""""""""""""""""""

def creteTableHash(m): 
    HashTable = [None] * m         #Creamos una tabla Hash con m elementos
    return HashTable                            #Estos elementos serán vacios []                        #CLAVE PRUEBA# AUN TENGO QUE AGREGAR ELEMENTOS UNU

""""""""""""""""""

def Hashing(keyvalue):
    suma=0
    for item in keyvalue:
        suma = suma + ord(item)
        
    key = (( ( ( 49 * suma ) + 689 ) % 999983 ) % len((tablaCreada)))
    return key
    
""""""""""""""""""

def insert(tablaCreada, keyvalue, nameValue):       #Inserta los elementos dentro de la tabla Hashing 
                                                #Recibe la tabla creada, el valor de la llave para insertar y value es el dato que va insertar 
    Lista = []
    hash_key = Hashing(keyvalue)

    if tablaCreada[hash_key] == None: 
        tablaCreada[hash_key] = Lista
                #La llave Hasheada 
    tablaCreada[hash_key].append(nameValue)
               #Se inserta value en tablaCreada en el indice de hash_key 

""""""""""""""""""

def searchElement(tablaCreada, keyvalue):

    hash_key = Hashing(keyvalue)

    if(tablaCreada[hash_key] is None):
        return None
    else:
        for item in tablaCreada [hash_key]:
            if item.username == keyvalue:
                return item
            
"""""""""""""""""" 

def login(tablaCreada, keyvalue, valuePasword):
    
    print("--------------------------------------------")
    print("LOGIN:   usr: " + keyvalue + "   pass: " + valuePasword)

    hash_key = Hashing(keyvalue)

    a = searchElement(tablaCreada, keyvalue)
    print(a)
    if (a == None): 
        print("Usuario no existe: ") 
    elif(a.password == valuePasword): 
        print("ACCESO concedido: ", a.fullname)       
    else: 
        print("Acceso no autorizado contraseña incorrecta") 

    print("--------------------------------------------")

"""""""""""""""""" 
def BusqLineal(list, keyusername):
    for k in range(0, len(list)):
        if ( list[k] is not None ):
            for j in range(0 , len(list[k])):
                if list[k][j].username == keyusername:
                    return list[k][j]
        else: continue
    return None

""""""""""""""""""
def Compare(tablaHash, usrList):
    sumLineal = sumHash = 0
    for i in range(10):
        usr = usrList[random.randint(0, len(usrList))].username
        t1 = time.perf_counter()
        e1 = searchElement(tablaHash, usr)
        t2 = time.perf_counter()

        t3 = time.perf_counter()
        e2 = BusqLineal(tablaHash, usr)
        t4 = time.perf_counter()
        print("\nPara encontrar al usuario: "+ usr + " tardé:")
        print("Con Busqueda Lineal:", t4 - t3, "\t Con Busqueda en Tabla Hash:", t2 - t1)
        sumLineal += t4 - t3
        sumHash += t2 - t1
    print("\nEl tiempo promedio de 10 casos fue de: ")    
    print("Para la Busqueda Lineal:", sumLineal/10)
    print("Para la Busqueda en Tabla Hash:", sumHash/10)

""""""""""""""""""
tablaCreada= creteTableHash(999)
usrList = Database.Usuario.GetUsuariosDB(1000)


for item in usrList:
    insert(tablaCreada, item.username, item)

login(tablaCreada, "mvicker23", "TNqqef")
login(tablaCreada, "tnewborn6x", "FnZzuo")
login(tablaCreada, "tnewborn6x", "123123")
login(tablaCreada, "Jesus Cruz", "123123")

print("Parámetros utilizados: \n a = 49\n b = 689\n p = 999983\n m (tamaño tabla) =", len(tablaCreada))
f = len(usrList)/len(tablaCreada)
print("Factor de carga: F =", f,"\n")

Compare(tablaCreada, usrList)


print("-----------------------------------")      
