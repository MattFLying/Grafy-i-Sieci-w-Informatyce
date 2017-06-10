'''
Created on 27.05.2017

@author: Mateusz Mucha
'''
from _model_._files import file as _file_
from _model_._graph import graph as _graph_


GRAPH_FILE_PATH = "F:\GitHub\GiSwI\_model_\_files\_lists_\graph_file_task_1_v1.txt"
GRAPH_FILE_MODE = 'r'
GRAPH_FILE = _file_.readFile(GRAPH_FILE_PATH, GRAPH_FILE_MODE)
FILE_DESCRIPTION = "Plik uzyty do wczytania grafu: " + str(GRAPH_FILE.name)
GRAPH_DICTIONARY = _file_.convertGraphFileIntoDictionary(GRAPH_FILE)
GRAPH = _graph_.Graph(GRAPH_DICTIONARY, 1)
GRAPH_EDGE_SEPARATOR = GRAPH.GRAPH_EDGE_SEPARATOR

'''
Help methods.
'''
def comma_string(collection_):
    buildedString_ = ", ".join(collection_)
    
    return buildedString_ 

def replacing(value, replaceType):
    if replaceType == '1':
        return str(value) \
                .replace("[", "| ") \
                .replace("]", " |") \
                .replace(", ", " ")
    elif replaceType == '2':
        return str(value) \
                .replace("[", "") \
                .replace("]", "")
    else:
        return "Wrong task replacing type."

def build_array(array, element):
    array.append(element)                

def adjacency_matrix(edgesCollection_, size_):
    
    matrix = [[0 for leftVertice in range(size_)] for rightVertice in range(size_)]  
    for edge in edgesCollection_:
        text = edge.split(GRAPH_EDGE_SEPARATOR)
        leftVertice = int(text[0])
        rightVertice = int(text[1])
        
        matrix[leftVertice - 1][rightVertice - 1] = 1
        matrix[rightVertice - 1][leftVertice - 1] = 1
        
    return matrix 

def incidency_matrix(edgesCollection_, vertices_, edges_):
    
    matrix = [[0 for leftVertice in range(vertices_)] for rightVertice in range(edges_)]
    counter = 0  
    for edge in edgesCollection_:
        text = edge.split(GRAPH_EDGE_SEPARATOR)
        leftVertice = int(text[0])
        rightVertice = int(text[1])
        
        matrix[leftVertice - 1][counter] = 1
        matrix[rightVertice - 1][counter] = 1       
        counter += 1
        
    return matrix 

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

def simple_graph():
    
    edges = GRAPH.getEdgesCollection()
    repeatableEdges = []    
    for edge in edges:
        text = edge.split(GRAPH_EDGE_SEPARATOR)   
        firstCombination = GRAPH_EDGE_SEPARATOR.join([text[0], text[1]])
        secondCombination = GRAPH_EDGE_SEPARATOR.join([text[1], text[0]])
        thirdCombination = GRAPH_EDGE_SEPARATOR.join([text[0], text[0]])
        fourCombination = GRAPH_EDGE_SEPARATOR.join([text[1], text[1]])
        
        edges.remove(edge)    
        for nextEdge in edges:
            if (nextEdge == firstCombination) or \
                (nextEdge == secondCombination) or \
                (nextEdge == thirdCombination) or \
                (nextEdge == fourCombination):
                
                repeatableEdges.append(nextEdge)
            if (nextEdge == thirdCombination) or \
                (nextEdge == fourCombination):
                
                if nextEdge not in repeatableEdges:
                    repeatableEdges.append(nextEdge)

    return repeatableEdges

def edges_dictionary():
    
    edges = GRAPH.getEdgesCollection()
    vertices = GRAPH.getUniqueVertices()
    edgesDictionary = {}
    
    for vertice in vertices:
        edgesDictionary[vertice] = []    
    for edge in edges:
        text = edge.split(GRAPH_EDGE_SEPARATOR)   
        firstCombination = text[0] + GRAPH_EDGE_SEPARATOR + text[1]
        secondCombination = text[1] + GRAPH_EDGE_SEPARATOR + text[0]
    
        edgesDictionary[text[0]].append(firstCombination)  
        edgesDictionary[text[1]].append(secondCombination) 
    
    return edgesDictionary

def check_missing_connection():
    
    vertices = GRAPH.getUniqueVertices()  
    missingConnections = [] 
    allEdges = edges_dictionary()
    
    for edge in sorted(allEdges.keys()):
        values = allEdges.get(edge)        
        if len(values) < (len(vertices) - 1):
            connections = []
            removingCheckingElement = \
                allEdges.get(edge)[0].split(GRAPH_EDGE_SEPARATOR)
            
            for connection in vertices:
                if removingCheckingElement[0] != connection:
                    connections.append(connection)           
            for value in values:
                checkingConnection = value.split(GRAPH_EDGE_SEPARATOR)           
            
                if checkingConnection[1] in connections:
                    connections.remove(checkingConnection[1])
                    
            for connection in connections:
                firstCombination = str(removingCheckingElement[0]) \
                    + GRAPH_EDGE_SEPARATOR \
                    + str(connection)
                secondCombination = str(connection) \
                    + GRAPH_EDGE_SEPARATOR \
                    + str(removingCheckingElement[0])
                
                missingConnections.append(firstCombination)
                allEdges[str(connection)] += secondCombination
            
    return missingConnections  

'''
Methods representing 5 tasks from laboratory list.
'''  
def task_one():
    
    result = ""    
    _description = []
    
    build_array(_description, FILE_DESCRIPTION)  
    build_array(_description, "\n\nLiczba wierzcholkow grafu G wynosi: ")
    build_array(_description, str(len(GRAPH.getUniqueVertices())))
    build_array(_description, "\nZbior wierzcholkow V = { ")
    build_array(_description, comma_string(GRAPH.getUniqueVertices()))
    build_array(_description, " }\n\nLiczba krawedzi grafu G wynosi: ")
    build_array(_description, str(GRAPH.getEdges()))
    build_array(_description, "\nZbior krawedzi E = { ")
    build_array(_description, comma_string(GRAPH.getEdgesCollection()))
    build_array(_description, " }\n\nMacierz sasiedztwa A = \n")

    for element in adjacency_matrix(GRAPH.getEdgesCollection(),
                                    int(GRAPH.getVertices())):
        build_array(_description, replacing(element, '1'))
        build_array(_description, "\n")   
    build_array(_description, "\nMacierz incydencji M = \n") 
    for element in incidency_matrix(GRAPH.getEdgesCollection(),
                                    int(GRAPH.getEdges()),
                                    int(GRAPH.getVertices())):
        build_array(_description, str(replacing(element, '1')))
        build_array(_description, "\n")
    
    result = result.join(_description)

    return result

def task_two():
    
    result = ""    
    _description = []
    dictionary = graph_degree(
        GRAPH.getEdgesCollection(), int(GRAPH.getVertices())
    )
    degreeSeries = sorted(dictionary.values())

    build_array(_description, FILE_DESCRIPTION)
    build_array(_description, "\n\nRzad grafu wynosi: ")
    build_array(_description, str(GRAPH.getGraphOrder()))
    build_array(_description, "\n\nRozmiar grafu wynosi: ")
    build_array(_description, str(GRAPH.getGraphSize()))
    build_array(_description, "\n\nStopnie wierzcholkow: ")
  
    for i in dictionary.keys():
        build_array(_description, "\ndet(")
        build_array(_description, str(i))
        build_array(_description, ") = ")
        build_array(_description, str(dictionary.get(i)))
        
    build_array(_description, "\n\nCiag stopni grafu: ")
    build_array(_description, replacing(degreeSeries, '2'))
    
    result = result.join(_description)
    
    return result

def task_three():
    
    result = ""    
    _description = []
    
    build_array(_description, FILE_DESCRIPTION)
    build_array(_description, "\n\nGraf G jest grafem ")

    if len(simple_graph()) > 0:
        build_array(_description, "ogolnym.")
    else:
        build_array(_description, "prostym.")
    
    result = result.join(_description)
    
    return result

def task_four():
    
    result = ""    
    _description = []
    connections = check_missing_connection()
    
    build_array(_description, FILE_DESCRIPTION)
    
    if len(simple_graph()) == 0:
        if len(connections) > 0:
            build_array(
                _description,
                "\n\nGraf G nie jest grafem pelnym. \
                \n\nKrawedzie dopelnienia grafu G: "
            )
            
            for missed in connections:
                build_array(_description, missed)
                build_array(_description, ", ")
    
    result = result.join(_description)
    
    return result[:-2]

def task_five():
    
    result = ""    
    _description = []
    edges = edges_dictionary()

    build_array(_description, FILE_DESCRIPTION)    
    for vertice in sorted(edges.keys()):   
        build_array(_description, "\n")
        build_array(_description, vertice)
        build_array(_description, " -> ")

        vertices = []
        for connections in sorted(edges.get(vertice)):
            connection = connections.split(GRAPH_EDGE_SEPARATOR)

            vertices.append(str(connection[1]))

        build_array(_description, comma_string(sorted(vertices)))  

    result = result.join(_description)
    
    return result
