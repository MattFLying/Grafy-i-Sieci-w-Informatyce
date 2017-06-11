'''
Created on 27.05.2017

@author: Mateusz Mucha
'''
def readWriteFile(fullPath, mode):
    
    if mode == 'r':
        return open(fullPath, "r")
    elif mode == 'w':
        return open(fullPath, "w")
    else:
        print("Wrong mode type.")

def createGraphFile(path, name, text):
    file_extension = ".txt"
    file_full_path = path + str("/") + name + file_extension
    
    edges_separator = " -- "
    textArray = []
    result = ""
    
    textArray.append("graph ")
    textArray.append(name.upper())
    textArray.append(" {")
    
    for i in text:
        edges = "\n    " + str(i[0]) + edges_separator + str(i[1]) + str(";")
        textArray.append(edges)

    textArray.append("\n}")
    
    createFile = readWriteFile(file_full_path, 'w')
    
    result = result.join(textArray)
    createFile.write(result)
    
    createFile.close() 
       
def convertGraphFileIntoDictionary(file):
    
    tupleTemp = tuple(file.read().split())    
    dictionaryGraph = {}
    
    dictionaryGraph['v'] = tupleTemp[0]
    dictionaryGraph['e'] = tupleTemp[1]
    dictionaryGraph['all'] = tupleTemp[2:]
    
    del tupleTemp
    
    return dictionaryGraph;

def convertGraphFileIntoDictionaryGraphvizStyle(file):
    
    tupleTemp = tuple(file.read().split())    
    dictionaryGraph = {}
    
    dictionaryGraph['name'] = tupleTemp[1]
    dictionaryGraph['edges'] = tupleTemp[3:-1]
    
    del tupleTemp
    
    return dictionaryGraph;
