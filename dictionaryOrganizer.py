#Modulo dictionaryOrganizer
def getWord(file, n):
    infile = open(file)
    i = 1
    line = infile.readline()
    while i < n:
        line = infile.readline()
        i += 1
    infile.close()
    return line

def nLines(file):
    infile = open(file)
    n = 0
    line = infile.readline()
    while line != "":
        n += 1
        line = infile.readline()
    infile.close()
    return n