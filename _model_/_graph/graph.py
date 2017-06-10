'''
Created on 27.05.2017

@author: Mateusz Mucha
'''
class Graph:
    
    
    def __init__(self, dictionary, graphTaskType):
        
        self.__graphTaskType = graphTaskType
        if self.__graphTaskType == 1:
            self.__edges = dictionary['e']
            self.__vertices = dictionary['v'] 
            self.__allEdges = dictionary['all']
            self.GRAPH_EDGE_SEPARATOR = "-"
        elif self.__graphTaskType == 2:
            self.__name = dictionary['name']
            self.__allEdges = dictionary['edges']
            self.GRAPH_EDGE_SEPARATOR = " -- "
    
    
    def getName(self):
        
        return self.__name
    
    def getEdges(self):
        
        return self.__edges
    
    
    def getVertices(self):
        
        return self.__vertices 
     
           
    def getAllEdges(self):
        
        return self.__allEdges
    
    
    def getUniqueVertices(self):
        
        if self.__graphTaskType == 1:
            return sorted(set(self.getAllEdges()))
        if self.__graphTaskType == 2:
            tab = []
            for i in self.getEdgesCollection():
                tab += i[0]
                tab += i[5]
            
            return sorted(set(tab))
    
    
    def getEdgesCollection(self):
        
        size = len(self.getAllEdges())
        edgesCollection = []
        count = 0; 
        
        if self.__graphTaskType == 1:
            while (count < size):
                edgesCollection += [
                    self.getAllEdges()[count] 
                    + self.GRAPH_EDGE_SEPARATOR
                    + self.getAllEdges()[count + 1]
                ]
                count += 2
                
            return edgesCollection
    
        elif self.__graphTaskType == 2:
            while (count < size):
                edgesCollection += [
                    self.getAllEdges()[count] 
                    + self.GRAPH_EDGE_SEPARATOR
                    + self.getAllEdges()[count + 2][:-1]
                ]
                count += 3
            
            
            
            return edgesCollection
    
    def getGraphOrder(self):
        
        return self.__vertices
    
    
    def getGraphSize(self):
        
        return self.__edges
