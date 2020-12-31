from typing import TextIO

def getStringInformation(file: TextIO):
    def printInfo(*toPrint):
        stringIndormation = " ".join([str(element) for element in toPrint])
        print(stringIndormation)
        file.write(stringIndormation + "\n")
    return printInfo

