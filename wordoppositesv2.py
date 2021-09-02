# not finished
wordData = []

with open('wordData.txt') as f:
    allLines = f.readlines()

    for line in range(1, len(allLines)):
        string = allLines[line]
        typeOfWord = allLines[line].find("KEY:") or allLines[line].find("SYN:") or allLines[line].find("ANT:")

        if "KEY:" in string:
            wordData.append([[][][]]
        


wordData = []
