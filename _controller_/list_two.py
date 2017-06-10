'''
Created on 10.06.2017

@author: Mateusz Mucha
'''
from _model_._files import file as _file_
from _model_._graph import graph as _graph_


GRAPH_FILE_PATH = "F:\GitHub\GiSwI\_model_\_files\_lists_\graph_file_task_2_v1.txt"
GRAPH_FILE_MODE = 'r'
GRAPH_FILE = _file_.readFile(GRAPH_FILE_PATH, GRAPH_FILE_MODE)
FILE_DESCRIPTION = "Plik uzyty do wczytania grafu: " + str(GRAPH_FILE.name)
GRAPH_DICTIONARY = _file_.convertGraphFileIntoDictionaryGraphvizStyle(GRAPH_FILE)
GRAPH = _graph_.Graph(GRAPH_DICTIONARY, 2)
GRAPH_EDGE_SEPARATOR = GRAPH.GRAPH_EDGE_SEPARATOR


'''
Help methods.
'''
def build_array(array, element):
    array.append(element)  
    
def edges_dictionary():
    
    edges = GRAPH.getEdgesCollection()
    vertices = GRAPH.getUniqueVertices()
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

def dfs_paths(graph, root, target, path=None):
    if path is None:
        path = [root]
        
    if root == target:
        yield path
            
    for vertex in [x for x in graph[root] if x not in path]:
        for each_path in dfs_paths(graph, vertex, target, path + [vertex]):
            yield each_path

def graph_degree(edgesCollection_, vertices_):
    
    dictionary = {} 
    for leftVertice in range(1, vertices_ + 1):
        dictionary[leftVertice] = 0        
    for edge in edgesCollection_:
        text = edge.split(GRAPH_EDGE_SEPARATOR)
        leftVertice = int(text[0])
        rightVertice = int(text[1])
        
        dictionary[leftVertice] += 1
        dictionary[rightVertice] += 1

    return dictionary


'''
Methods representing 5 tasks from laboratory list.
''' 
def task_one():
    
    result = ""    
    _description = []
    
    build_array(_description, FILE_DESCRIPTION)  
    dictionary = graph_degree(
        GRAPH.getEdgesCollection(), int(len(GRAPH.getUniqueVertices()))
    )
    regular_checking = []
    
    build_array(_description, "\n\nWierzcholki, ich polaczenia oraz stopnie:")
    for i in sorted(edges_dictionary()):
        build_array(_description, "\n")
        build_array(_description, str(i))
        build_array(_description, ": ")
        build_array(_description, str(edges_dictionary().get(i)))
        
        for j in dictionary.keys():
            if i == j:
                build_array(_description, ", Stopien wierzcholka: det(")
                build_array(_description, str(j))
                build_array(_description, ") = ")
                build_array(_description, str(dictionary.get(j)))
                
                regular_checking.append(dictionary.get(j))
    
    maxDegree = max(regular_checking)
    count = 0
    for i in regular_checking:
        if i < maxDegree:
            count += 1
            
    build_array(_description, "\n\nGraf ")
    build_array(_description, GRAPH.getName())
    build_array(_description, " jest grafem ")
    
    if count > 0:
        build_array(_description, "nieregularnym gdyz ")
        build_array(_description, str(count))
        build_array(_description, " wierzcholki sa rozne.")
    else:
        build_array(_description, "regularnym ")
        build_array(_description, str(maxDegree))
        build_array(_description, "-go stopnia.")
    
    result = result.join(_description)
    
    return result             

def task_two():
    
    result = ""    
    _description = []
    
    minV = int(min(GRAPH.getUniqueVertices()))
    maxV = int(max(GRAPH.getUniqueVertices()))
    list1 = list(dfs_paths(edges_dictionary(), minV, maxV))
    list2 = list(dfs_paths(edges_dictionary(), maxV, minV))
    maxPath = min(list1)
    
    build_array(_description, FILE_DESCRIPTION)  
    build_array(_description, "\n\nWszystkie mozliwe sciezki w grafie ")
    build_array(_description, GRAPH.getName())
    build_array(_description, ": \n")
    
    count = 0
    for i in list1:
        count += 1
        build_array(_description, "Sciezka: ")
        build_array(_description, str(count))
        build_array(_description, ": ")
        build_array(_description, str(i))
        build_array(_description, "\n")   
    
    
    
    count = 0
    for i in GRAPH.getUniqueVertices():
        if int(i) in maxPath:
            count += 1
    
    edgeCheck1 = str(maxPath[0]) + GRAPH_EDGE_SEPARATOR + str(maxPath[-1])
    edgeCheck2 = str(maxPath[-1]) + GRAPH_EDGE_SEPARATOR + str(maxPath[0])
    
    if edgeCheck1 or edgeCheck2 in GRAPH.getEdgesCollection():
        if maxPath[-2] != minV:
            print()
    
    
    
    
    
    result = result.join(_description)
    
    return result 









print(task_two())








