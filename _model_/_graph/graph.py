'''
Created on 27.05.2017

@author: Mateusz Mucha
'''
class Graph:
    
    
    def __init__(self, dictionary):
        
        self.__edges = dictionary['e']
        self.__vertices = dictionary['v'] 
        self.__allEdges = dictionary['all']
        self.GRAPH_EDGE_SEPARATOR = "-"
    
    
    def getEdges(self):
        
        return self.__edges
    
    
    def getVertices(self):
        
        return self.__vertices 
     
           
    def getAllEdges(self):
        
        return self.__allEdges
    
    
    def getUniqueVertices(self):
        
        return sorted(set(self.getAllEdges()))
    
    
    def getEdgesCollection(self):
        
        size = len(self.getAllEdges())
        edgesCollection = []
        count = 0;        
        
        while (count < size):
            edgesCollection += [
                self.getAllEdges()[count] 
                + self.GRAPH_EDGE_SEPARATOR
                + self.getAllEdges()[count + 1]
            ]
            count += 2
            
        return edgesCollection
    
    
    def getGraphOrder(self):
        
        return self.__vertices
    
    
    def getGraphSize(self):
        
        return self.__edges
