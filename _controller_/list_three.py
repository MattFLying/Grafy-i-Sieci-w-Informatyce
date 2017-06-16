'''
Created on 13.06.2017

@author: Mateusz Mucha
'''
from _model_._files import file as _file_
from _model_._graph import graph as _graph_
import networkx as nx
from tsp_solver.greedy import solve_tsp


GRAPH_FILE_PATH = "F:\GitHub\GiSwI\_model_\_files\_lists_\graph_file_task_3_v1.txt"
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
    
def edges_dictionary(edges_, vertices_):
    
    edges = edges_
    vertices = vertices_
    edgesDictionary = {}
    
    for vertice in vertices:
        edgesDictionary[int(vertice)] = []    
    for edge in edges:
        text = edge.split(GRAPH_EDGE_SEPARATOR) 
        
        firstCombination = int(text[1])
        secondCombination = int(text[0])
    
        edgesDictionary[secondCombination].append(firstCombination)  
        edgesDictionary[firstCombination].append(secondCombination) 
    
    return edgesDictionary






def task_one():
    result = ""    
    _description = []
    
    build_array(_description, FILE_DESCRIPTION) 
    edgesCollection = GRAPH.getEdgesCollection()
    weightDictionary = GRAPH.getGraphWeights()
    build_array(_description, "\n\n")
    
    file_path = "F:\GitHub\GiSwI\_model_\_files\_lists_"  
    GRAPH.setName("G")  
    _file_.createGraphFileWeights(file_path, GRAPH.getName(), weightDictionary)
    
    build_array(_description, "Zbudowano nastepujaca strukture pliku:\n\ngraph ")
    build_array(_description, GRAPH.getName())
    build_array(_description, " {")
    for i in weightDictionary:
        build_array(_description, "\n    ")
        build_array(_description, str(i[0]))
        build_array(_description, GRAPH_EDGE_SEPARATOR)
        build_array(_description, str(i[5]))
        build_array(_description, str(' [label="'))
        build_array(_description, str(weightDictionary.get(i)))
        build_array(_description, str('"];'))
    
    build_array(_description, "\n}")
    
    
    result = result.join(_description)
    
    return result 

def task_two(): 
    edgesCollection = GRAPH.getEdgesCollection()
    weightDictionary = GRAPH.getGraphWeights()
    
    print(FILE_DESCRIPTION + "\n")
    firstV = int(input("Podaj numer pierwszego wierzcholka[1 do 4]: "))
    secondV = int(input("Podaj numer drugiego wierzcholka[1 do 4]: "))
    
    graph = nx.Graph()
    for i in weightDictionary:
        s = i.split()
        v1 = s[0]
        v2 = s[2]
        weight = weightDictionary.get(i)
        graph.add_edge(int(v1), int(v2), weight=int(weight))     
        
    print("\nNajkrotsza droga pomiedzy wierzcholkami " + str(firstV) + " i " + str(secondV) + " to: " + str(nx.dijkstra_path(graph, firstV, secondV)))
    print("Najkrotsza droga pomiedzy wierzcholkami " + str(firstV) + " i " + str(secondV) + " wynosi: " + str(nx.dijkstra_path_length(graph, firstV, secondV)))
    
def task_three(): 
    result = ""    
    _description = []
    
    build_array(_description, FILE_DESCRIPTION)
    build_array(_description, "\n\n")
    
    edgesCollection = GRAPH.getEdgesCollection()
    weightDictionary = GRAPH.getGraphWeights()
    build_array(_description, "Najkrotsza droga pomiedzy wierzcholkami (w1-w2 droga):\n")
    
    graph = nx.Graph()
    for i in weightDictionary:
        s = i.split()
        v1 = s[0]
        v2 = s[2]
        weight = weightDictionary.get(i)
        graph.add_edge(int(v1), int(v2), weight=int(weight)) 
        
    edges = graph.nodes()
    newDdgesCollection = []
    for i in graph.nodes():
        for j in edges:
            if j > i:
                text = str(i) + " -- " + str(j)
                newDdgesCollection.append(text)
                
                
    for i in newDdgesCollection:
        s = i.split()
        firstV = s[0]
        secondV = s[2]
        
        build_array(_description, firstV)
        build_array(_description, "-")
        build_array(_description, secondV)
        build_array(_description, "    ")
        build_array(_description, str(nx.dijkstra_path_length(graph, int(firstV), int(secondV))))
        build_array(_description, "\n")

    
    result = result.join(_description)
    
    return result 
    
def task_four(): 
    GRAPH_FILE_PATH = "F:\GitHub\GiSwI\_model_\_files\_lists_\komiwojazer.txt"
    GRAPH_FILE_MODE = 'r'
    GRAPH_FILE = _file_.readWriteFile(GRAPH_FILE_PATH, GRAPH_FILE_MODE)
    FILE_DESCRIPTION = "Plik uzyty do wczytania grafu: " + str(GRAPH_FILE.name)
    GRAPH_DICTIONARY = _file_.convertGraphFileIntoDictionary(GRAPH_FILE)
    GRAPH = _graph_.Graph(GRAPH_DICTIONARY, 3)
    GRAPH_EDGE_SEPARATOR = GRAPH.GRAPH_EDGE_SEPARATOR
    
    result = ""    
    _description = []
    
    print(FILE_DESCRIPTION + "\n")
    city = str(input("Podaj miasto, z ktorego i do ktorego chcesz znalezc sciezke: "))
    cityArray = list(city)
    cityArray[0] = cityArray[0].upper()
    for i in cityArray[1:]:
        i = i.lower()
    city = "".join(cityArray)
    
    edgesCollection = GRAPH.getEdgesCollection()
    weightDictionary = GRAPH.getGraphWeights()
    
    graph = nx.Graph()
    for i in weightDictionary:
        s = i.split()
        v1 = s[0]
        v2 = s[2]
        weight = weightDictionary.get(i)
        graph.add_edge(v1, v2, weight=int(weight)) 
        
    
    nodes = graph.nodes() 
    nodes.remove(city)  
    lowest = 0   
    biggest = 0
    equaling = 0  
    pathsDict = {}
    
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
    
    build_array(_description, "\n\nNajkrotsza droga dla miasta ")
    build_array(_description, str(city))
    build_array(_description, " to: \n")
    count = 0
    for i in pathsDict.get(lowest):
        build_array(_description, str(i))
        count += 1
        if count < len(pathsDict.get(lowest)):
            build_array(_description, str(" -> "))
    
    build_array(_description, str("\nI wynosi: "))
    build_array(_description, str(lowest))
    
    build_array(_description, "\n\nNajdluzsza droga dla miasta ")
    build_array(_description, str(city))
    build_array(_description, " to: \n")
    count = 0
    for i in pathsDict.get(biggest):
        build_array(_description, str(i))
        count += 1
        if count < len(pathsDict.get(biggest)):
            build_array(_description, str(" -> "))
    
    build_array(_description, str("\nI wynosi: "))
    build_array(_description, str(biggest))
    
    
    result = result.join(_description)
    
    createFile = open("F:\GitHub\GiSwI\_model_\_files\_lists_\komiwojazer_paths.txt", 'w')
    for i in sorted(pathsDict):
        createFile.write(str(i))
        createFile.write(str(" :: "))
        createFile.write(str(pathsDict.get(i)))
        createFile.write(str("\n"))
    createFile.close() 
    
    
    return result    
    
def task_five(): 
    GRAPH_FILE_PATH = "F:\GitHub\GiSwI\_model_\_files\_lists_\graf_pelny.txt"
    GRAPH_FILE_MODE = 'r'
    GRAPH_FILE = _file_.readWriteFile(GRAPH_FILE_PATH, GRAPH_FILE_MODE)
    FILE_DESCRIPTION = "Plik uzyty do wczytania grafu: " + str(GRAPH_FILE.name)
    GRAPH_DICTIONARY = _file_.convertGraphFileIntoDictionary(GRAPH_FILE)
    GRAPH = _graph_.Graph(GRAPH_DICTIONARY, 3)
    GRAPH_EDGE_SEPARATOR = GRAPH.GRAPH_EDGE_SEPARATOR
    
    result = ""    
    _description = []
    
    print(FILE_DESCRIPTION + "\n")
    city = str(input("Podaj wierzcholek[1 do 5], z ktorego i do ktorego chcesz znalezc sciezke: "))
    
    edgesCollection = GRAPH.getEdgesCollection()
    weightDictionary = GRAPH.getGraphWeights()
    
    graph = nx.Graph()
    for i in weightDictionary:
        s = i.split()
        v1 = s[0]
        v2 = s[2]
        weight = weightDictionary.get(i)
        graph.add_edge(v1, v2, weight=float(weight)) 
        
    
    nodes = graph.nodes() 
    nodes.remove(city)  
    lowest = 0   
    biggest = 0
    equaling = 0  
    pathsDict = {}
    
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
    
    build_array(_description, "\n\nNajkrotsza droga dla miasta ")
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
    
    build_array(_description, "\n\nNajdluzsza droga dla miasta ")
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
    
    createFile = open("F:\GitHub\GiSwI\_model_\_files\_lists_\graf_pelny_paths.txt", 'w')
    for i in sorted(pathsDict):
        createFile.write(str("{0:.2f}".format(round(i, 2))))
        createFile.write(str(" :: "))
        createFile.write(str(pathsDict.get(i)))
        createFile.write(str("\n"))
    createFile.close() 
    
    
    return result    
