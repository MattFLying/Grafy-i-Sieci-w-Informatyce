'''
Created on 27.05.2017

@author: Mateusz Mucha
'''
def readFile(fullPath, mode):
    
    if mode == 'r':
        return open(fullPath, "r")
    elif mode == 'w':
        return open(fullPath, "w")
    else:
        print("Wrong mode type.")
  
       
def convertGraphFileIntoDictionary(file):
    
    tupleTemp = tuple(file.read().split())    
    dictionaryGraph = {}
    
    dictionaryGraph['v'] = tupleTemp[0]
    dictionaryGraph['e'] = tupleTemp[1]
    dictionaryGraph['all'] = tupleTemp[2:]
    
    del tupleTemp
    
    return dictionaryGraph;
