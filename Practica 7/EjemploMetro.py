from Grafo import Grafo 
from metro import lineas 

if __name__ == "__main__":

    lineasMetro = Grafo()

    for linea in lineas:
        for i in range(len(linea)):
            lineasMetro.addVertex(linea[i])
            if i != 0:
                lineasMetro.addBranch(linea[i], linea[i-1] )
    
    lineasMetro.RutaBFS("Pantitlán", "Insurgentes")
    lineasMetro.RutaDFS("Vallejo", "Insurgentes") 
    print("\t##########CAMBIANDO DE PRUEBA##########")
    lineasMetro.RutaBFS("Aquiles Serdán", "Iztapalapa")
    lineasMetro.RutaDFS("Aquiles Serdán", "Iztapalapa")
    print("\t##########CAMBIANDO DE PRUEBA##########")
    lineasMetro.RutaBFS("San Antonio", "Aragón")
    lineasMetro.RutaDFS("San Antonio", "Aragón")

    #print("\n--------------IMPRIMIENDO LINEAS DEL METRO:--------------------- \n", lineasMetro)

