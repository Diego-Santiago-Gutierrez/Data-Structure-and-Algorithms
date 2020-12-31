def parseCsv():
    with open("covid-19-mexico-01122020.csv", encoding='utf-8') as file:
        lines = file.read().splitlines()
        columnNames = lines[0].split(',')
        userInformation = []
        for i in range(1, len(lines)):
            information = lines[i].split(',')
            userInformation.append((information[0], information[1], information[2], int(information[3]), information[4], information[5]))

    return columnNames, userInformation
    