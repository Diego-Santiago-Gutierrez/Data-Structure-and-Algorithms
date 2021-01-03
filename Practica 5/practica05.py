import Database
from time import perf_counter
import sys
import random as rdn
import random
import time
#from Database import Usuario

   
""""""""""""""""""
#Creamoso tabla, m es el parametro de espacios
def creteTableHash(m): 
    HashTable = [ [] for a in range(m) ]        
    return HashTable              

""""""""""""""""""

#Hashing devuelve una key para acomodar dicho elemento
def Hashing(keyvalue):
    suma=0
    for item in keyvalue:
        suma = suma + ord(item)
        
    key = (( ( ( 49 * suma ) + 689 ) % 999983 ) % len((tablaCreada)))
    return key
    
""""""""""""""""""

#Insertamos los valores dentro de la tabla Hash 
def insert(tablaCreada, keyvalue, nameValue):       
                                                
    hash_key = Hashing(keyvalue)
    tablaCreada[hash_key].append(nameValue)
               
""""""""""""""""""

#Buscamos elemento sacando la Hash-key del elemento a buscar
#Después se realiza busqueda lineal 
def searchElement(tablaCreada, keyvalue):

    hash_key = Hashing(keyvalue)

    if(tablaCreada[hash_key] == []):
        return None
    else:
        for item in tablaCreada [hash_key]:
            if item.username == keyvalue:
                return item
            
"""""""""""""""""" 
#KeyValue -> UserName, valuePasword->Contraseña 
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
def BusqLineal(lista, keyusername):
    for k in range(len(lista)):
        if ( lista[k] != [] ):
            for j in range(len(lista[k])):
                if lista[k][j].username == keyusername:
                    return lista[k][j]

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
tablaCreada= creteTableHash(1000)
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
