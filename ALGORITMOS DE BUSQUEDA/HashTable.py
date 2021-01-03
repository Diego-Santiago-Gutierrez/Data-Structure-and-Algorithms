
def convCad(cad): 
    salida = "" 

    for i in cad: 
        salida += str(ord(i)) 
    
    return int(salida)

def hashM(cad, m):
    i = convCad(cad)

    return ( ( ( 49 * i ) + 689 ) % 999983 ) % len((ht))

def agregar(cad, ht, m): 
    res = hashM(cad, ht)
    ht[res].append(cad)

def buscar(cad, ht, m):
    h = hashM(cad, ht)
    
    for i in ht[h]:
        if i == cad: 
            return True

    return False

def eliminar(cad, ht, m):
    res = hashM(cad, ht)

    for i in ht[res]: 
        if i == cad: 
            a = ht[res].remove(cad)
            return a

        else: 
            print("No se pudo eliminar")
            return None
m = 19 

ht = [ [] for i in range(m) ]

agregar("Culo", ht, m)
agregar("bien", ht, m)
agregar("yolo", ht, m)
agregar("espero", ht, m)
agregar("estas", ht, m)
agregar("como", ht, m)
agregar("Hola", ht, m)
agregar("neib", ht, m)

print(ht)

print(buscar("nalgona", ht, m))
print(buscar("bien", ht, m))

print(eliminar("Culo", ht, m))
print(ht)