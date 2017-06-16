'''
Created on 14.06.2017

@author: Mateusz Mucha
'''
from _model_._files import file as _file_
from _model_._graph import graph as _graph_
import networkx as nx


GRAPH_FILE_PATH = "F:\GitHub\GiSwI\_model_\_files\_lists_\graph_file_task_4_v1.txt"
GRAPH_FILE_MODE = 'r'
GRAPH_FILE = _file_.readWriteFile(GRAPH_FILE_PATH, GRAPH_FILE_MODE)
FILE_DESCRIPTION = "Plik uzyty do wczytania grafu: " + str(GRAPH_FILE.name)
GRAPH_DICTIONARY = _file_.convertGraphFileIntoDictionary(GRAPH_FILE)
GRAPH = _graph_.Graph(GRAPH_DICTIONARY, 3)
GRAPH_EDGE_SEPARATOR = GRAPH.GRAPH_EDGE_SEPARATOR


'''
Help methods.
'''
def build_array(array, element):
    array.append(element)  

def task_one():
    result = ""    
    _description = []
    
    build_array(_description, FILE_DESCRIPTION) 
    build_array(_description, "\n")
    
    edgesCollection = GRAPH.getEdgesCollection()
    weightDictionary = GRAPH.getGraphWeights()
    pathsWeightDict = {}
    
    graph = nx.Graph()
    for i in weightDictionary:
        s = i.split()
        v1 = s[0]
        v2 = s[2]
        weight = weightDictionary.get(i)
        graph.add_edge(int(v1), int(v2), weight=int(weight)) 
    
    
    if nx.is_eulerian(graph):
        for i in graph.nodes():
            way = 0
            euler = list(nx.eulerian_circuit(graph, i))
            
            for j in euler:
                way += graph[j[0]][j[1]]['weight']
            
            pathsWeightDict[i] = [way, euler] 
        
          
        build_array(_description, str("\nGraf zawiera cykl Eulera, zatem najkrotsze mozliwe sciezki dla wszystkich wierzcholkow poczatkowych to:\n"))
        for i in pathsWeightDict:
            build_array(_description, str("\nWierzcholek: "))
            build_array(_description, str(i))
            build_array(_description, str(", Sciezka: "))
            build_array(_description, str(pathsWeightDict.get(i)[1]))
            build_array(_description, str(", Waga: "))
            build_array(_description, str(pathsWeightDict.get(i)[0])) 
        
        build_array(_description, str("\n\nChinski Listonosz moze wybrac dowolna sciezke z powyzszych."))   
        
        createFile = open("F:\GitHub\GiSwI\_model_\_files\_lists_\chinski_listonosz.txt", 'w')
        createFile.write(str("graph ChinskiListonosz {"))
        for i in graph.edges():
            createFile.write(str("\n    "))
            createFile.write(str(i[0]))
            createFile.write(str(" -- "))
            createFile.write(str(i[1]))
            createFile.write(str(" [label="))
            createFile.write(str(graph[i[0]][i[1]]['weight']))
            createFile.write(str('"];'))
        createFile.close() 
            
    else:
        build_array(_description, str("\nGraf nie zawiera cyklu Eulera. Wszystkie stopnie wierzcholkow: "))       
            
        nodesDegree = graph.degree()
        nodesOddDegres = {}            
        for i in nodesDegree:
            if nodesDegree.get(i) % 2 != 0:
                nodesOddDegres[int(i)] = nodesDegree.get(i)
            build_array(_description, str("\ndet(")) 
            build_array(_description, str(i)) 
            build_array(_description, str(") = ")) 
            build_array(_description, str(nodesDegree.get(i))) 
            
        build_array(_description, str("\n\nWszystkie nieparzyste stopnie wierzcholkow: ")) 
        for i in nodesOddDegres:
            build_array(_description, str("\ndet(")) 
            build_array(_description, str(i)) 
            build_array(_description, str(") = ")) 
            build_array(_description, str(nodesDegree.get(i))) 
            
        nodes = list(nodesOddDegres.keys())
        pathBetweenOddNodes = nx.dijkstra_path(graph, nodes[0], nodes[1])
        
        oddNodes = []
        for i in pathBetweenOddNodes:
            oddNodes.append(i)
            
        counter = 1
        oddEdges = []
        while(counter < len(oddNodes)):
            s = str(oddNodes[counter-1]) + " -- " + str(oddNodes[counter])
            oddEdges.append(s)
            counter += 1
        
        multiGraph = nx.MultiGraph()
        for i in graph.edges():
            tempWeight = graph[i[0]][i[1]]['weight']
            multiGraph.add_edge(i[0], i[1], weight=int(tempWeight))
        
        for i in oddEdges:
            s = i.split()
            weight = graph[int(s[0])][int(s[2])]['weight']
            multiGraph.add_edge(int(s[0]), int(s[2]), weight=int(weight))
    
        build_array(_description, str("\n\nNowo utworzony multigraf i stopnie jego wierzcholkow: ")) 
        newNodesDegree = multiGraph.degree()
        newNodesOddDegres = {}            
        for i in newNodesDegree:
            if newNodesDegree.get(i) % 2 != 0:
                newNodesOddDegres[int(i)] = newNodesDegree.get(i)
            build_array(_description, str("\ndet(")) 
            build_array(_description, str(i)) 
            build_array(_description, str(") = ")) 
            build_array(_description, str(newNodesDegree.get(i))) 
            
        for i in multiGraph.nodes():
            way = 0
            euler = list(nx.eulerian_circuit(multiGraph, i))
            
            for j in euler:
                way += multiGraph[j[0]][j[1]][0]['weight']
            
            pathsWeightDict[i] = [way, euler] 
        
        build_array(_description, str("\n\nTeraz graf zawiera cykl Eulera, zatem najkrotsze mozliwe sciezki dla wszystkich wierzcholkow poczatkowych to:"))
        for i in pathsWeightDict:
            build_array(_description, str("\nWierzcholek: "))
            build_array(_description, str(i))
            build_array(_description, str(", Sciezka: "))
            build_array(_description, str(pathsWeightDict.get(i)[1]))
            build_array(_description, str(", Waga: "))
            build_array(_description, str(pathsWeightDict.get(i)[0])) 
        
        build_array(_description, str("\n\nChinski Listonosz moze wybrac dowolna sciezke z powyzszych."))  
    
        createFile = open("F:\GitHub\GiSwI\_model_\_files\_lists_\chinski_listonosz.txt", 'w')
        createFile.write(str("graph ChinskiListonosz {"))
        for i in multiGraph.edges():
            createFile.write(str("\n    "))
            createFile.write(str(i[0]))
            createFile.write(str(" -- "))
            createFile.write(str(i[1]))
            createFile.write(str(" [label="))
            createFile.write(str(multiGraph[i[0]][i[1]][0]['weight']))
            createFile.write(str('"];'))
        createFile.close() 
    
    result = result.join(_description)
    
    return result 