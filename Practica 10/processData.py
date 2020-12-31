# pip install pandas
import pandas
import os

from parsing import parseCsv
from stringInfo import getStringInformation


def processData():
    columns, data = parseCsv()
    dataFrame = pandas.DataFrame(data, columns=columns)

    file = open("PracticaResumen/resumenCovid.eda2", "w")
    printFile = getStringInformation(file)

    printFile("\nTotal de casos:", len(dataFrame))

    printFile("\nCasos por estado:")
    states = dataFrame["Nom_Ent"].value_counts()
    printFile(states.to_string())

    printFile("\nEstado con más casos:", states.idxmax())
    printFile("Estado con menos casos:", states.idxmin())

    printFile("\nCasos por género")
    gender = dataFrame["SEXO"].value_counts()
    printFile(gender.to_string())

    printFile("\nPromedio de edad:", dataFrame["EDAD"].mean())
    printFile("\nEdad máxima:", dataFrame["EDAD"].max())
    printFile("Edad mínima:", dataFrame["EDAD"].min())

    file.close()


def createDir():
    # Crear directorio si no existe
    try:
        os.mkdir("PracticaResumen")
    except FileExistsError:
        print("El directorio PracticaResumen ya existe.")