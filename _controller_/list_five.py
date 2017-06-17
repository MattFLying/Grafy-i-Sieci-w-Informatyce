#!/usr/bin/python
'''
Created on 17.06.2017

@author: MatiM92
'''
import sys
import networkx as nx


def build_array(array, element):
    array.append(element) 

def loadGraphFromFile(file_full_path):
    file = open(file_full_path, 'r')
    
    tupleTemp = tuple(file.read().split())    
    dictionaryGraph = {}
    
    dictionaryGraph['v'] = tupleTemp[0]
    dictionaryGraph['e'] = tupleTemp[1]
    dictionaryGraph['all'] = tupleTemp[2:]
    
    del tupleTemp
    
    return dictionaryGraph;

def buildNxGraph(graphDict, weightType):
    graph = nx.Graph()
    counter = 0
    tempArray = []
    
    for i in graphDict['all']:
        tempArray.append(i)
    
    while(counter < len(tempArray)):
        if weightType == int:
            graph.add_edge(int(tempArray[counter]), int(tempArray[counter + 1]), weight=int(tempArray[counter + 2]))
        elif weightType == float:
            graph.add_edge(int(tempArray[counter]), int(tempArray[counter + 1]), weight=float(tempArray[counter + 2]))
        
        counter += 3

    return graph


def task_one():
    GRAPH_FILE_PATH = "F:/GitHub/GiSwI/_model_/_files/_lists_/"
    GRAPH_FILE_PATH += str(sys.argv[2])
    result = ""    
    _description = []
    
    
    graphDict = loadGraphFromFile(GRAPH_FILE_PATH)
    graph = buildNxGraph(graphDict, int)
    isConnected = nx.is_connected(graph)
    
    build_array(_description, str("\nCzy wybrany graf z pliku:\n")) 
    build_array(_description, str(GRAPH_FILE_PATH)) 
    build_array(_description, str("\njest grafem spojnym(zgodnie z zalozeniem zadania)? : ")) 
    build_array(_description, str(isConnected))
    
    if isConnected:
        build_array(_description, str("\n\nJego krawedzie oraz wagi:")) 
        for i in graph.edges():
            build_array(_description, "\n")
            build_array(_description, str(i))
            build_array(_description, str(" Waga: "))
            build_array(_description, str(graph[i[0]][i[1]]['weight']))
        
        firstV = int(sys.argv[3])
        secondV = int(sys.argv[4])
        
        build_array(_description, str("\n\nNajkrotsza droga pomiedzy wierzcholkami "))
        build_array(_description, str(firstV))
        build_array(_description, str(" i "))
        build_array(_description, str(secondV))
        build_array(_description, str(" to: "))
        build_array(_description, str(nx.dijkstra_path(graph, firstV, secondV)))
        
        build_array(_description, str("\nNajkrotsza droga pomiedzy wierzcholkami "))
        build_array(_description, str(firstV))
        build_array(_description, str(" i "))
        build_array(_description, str(secondV))
        build_array(_description, str(" wynosi: "))
        build_array(_description, str(nx.dijkstra_path_length(graph, firstV, secondV)))

    else:
        build_array(_description, str("\n\nGraf nie jest grafem spojnym!")) 

    result = result.join(_description)
    return result 

def task_two():
    GRAPH_FILE_PATH = "F:/GitHub/GiSwI/_model_/_files/_lists_/"
    GRAPH_FILE_PATH += str(sys.argv[2])
    result = ""    
    _description = []
    
    graphDict = loadGraphFromFile(GRAPH_FILE_PATH)
    graph = buildNxGraph(graphDict, float)
    
    city = int(sys.argv[3])
    
    nodes = graph.nodes() 
    nodes.remove(city)  
    lowest = 0   
    biggest = 0
    equaling = 0  
    pathsDict = {}
    
    build_array(_description, str("\n\nKrawedzie oraz wagi wczytanego grafu pelnego:")) 
    for i in graph.edges():
        build_array(_description, "\n")
        build_array(_description, str(i))
        build_array(_description, str(" Waga: "))
        build_array(_description, str(graph[i[0]][i[1]]['weight']))
    
    for i in nodes: 
        for j in nx.all_simple_paths(graph, source=city, target=i):
            if len(j) > len(nodes):
                way = 0
                counter = 1
                
                while(counter < len(j)):
                    way += graph[j[counter - 1]][j[counter]]['weight']
                    counter += 1
                way += graph[j[-1]][city]['weight']
                j.append(city)
                
                if equaling < 1:
                    lowest = way
                    biggest = way
                    equaling += 1
                elif way < lowest:
                    lowest = way
                elif way > biggest:
                    biggest = way
                
                pathsDict[way] = j
    
    build_array(_description, "\n\nProblem komiwojazera - Najkrotsza droga dla wierzcholka ")
    build_array(_description, str(city))
    build_array(_description, " to: \n")
    count = 0
    for i in pathsDict.get(lowest):
        build_array(_description, str(i))
        count += 1
        if count < len(pathsDict.get(lowest)):
            build_array(_description, str(" -> "))
    
    build_array(_description, str("\nI wynosi: "))
    build_array(_description, str("{0:.2f}".format(round(lowest, 2))))
    
    build_array(_description, "\n\nProblem komiwojazera - Najdluzsza droga dla wierzcholka ")
    build_array(_description, str(city))
    build_array(_description, " to: \n")
    count = 0
    for i in pathsDict.get(biggest):
        build_array(_description, str(i))
        count += 1
        if count < len(pathsDict.get(biggest)):
            build_array(_description, str(" -> "))
    
    build_array(_description, str("\nI wynosi: "))
    build_array(_description, str("{0:.2f}".format(round(biggest, 2))))
    

    result = result.join(_description)
    return result 

def task_three():
    GRAPH_FILE_PATH = "F:/GitHub/GiSwI/_model_/_files/_lists_/"
    GRAPH_FILE_PATH += str(sys.argv[2])
    result = ""    
    _description = []
    
    city = int(sys.argv[3])
    graphDict = loadGraphFromFile(GRAPH_FILE_PATH)
    graph = buildNxGraph(graphDict, int)
    pathsWeightDict = {}
    
    if nx.is_eulerian(graph):
        for i in graph.nodes():
            way = 0
            euler = list(nx.eulerian_circuit(graph, i))
            
            for j in euler:
                way += graph[j[0]][j[1]]['weight']
            
            pathsWeightDict[i] = [way, euler] 

        build_array(_description, str("\n\nProblem chinskiego listonosza:"))
        build_array(_description, str("\nGraf zawiera cykl Eulera, zatem najkrotsze mozliwe sciezki dla wszystkich wierzcholkow poczatkowych to:\n"))
        for i in pathsWeightDict:
            build_array(_description, str("\nWierzcholek: "))
            build_array(_description, str(i))
            build_array(_description, str("\nSciezka: "))
            build_array(_description, str(pathsWeightDict.get(i)[1]))
            build_array(_description, str("\nWaga: "))
            build_array(_description, str(pathsWeightDict.get(i)[0])) 
        
      
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
            s = str(oddNodes[counter - 1]) + " -- " + str(oddNodes[counter])
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
        
        build_array(_description, str("\n\nProblem chinskiego listonosza:"))
        build_array(_description, str("\nTeraz graf zawiera cykl Eulera, zatem najkrotsza mozliwa sciezka dla wierzcholka ")) 
        build_array(_description, str(city))
        build_array(_description, str(" to: "))
        build_array(_description, str("\nSciezka: "))
        build_array(_description, str(pathsWeightDict.get(city)[1]))
        build_array(_description, str("\nWaga: "))
        build_array(_description, str(pathsWeightDict.get(city)[0]))        


    result = result.join(_description)
    return result 


def main():
    if sys.argv[1] == "zad1":
        print(task_one())
    if sys.argv[1] == "zad2":
        print(task_two())
    if sys.argv[1] == "zad3":
        print(task_three())
        
if __name__ == "__main__":
    main()
