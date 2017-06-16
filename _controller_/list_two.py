'''
Created on 10.06.2017

@author: Mateusz Mucha
'''
from _model_._files import file as _file_
from _model_._graph import graph as _graph_


GRAPH_FILE_PATH = "F:\GitHub\GiSwI\_model_\_files\_lists_\graph_file_task_2_v1.txt"
GRAPH_FILE_MODE = 'r'
GRAPH_FILE = _file_.readWriteFile(GRAPH_FILE_PATH, GRAPH_FILE_MODE)
FILE_DESCRIPTION = "Plik uzyty do wczytania grafu: " + str(GRAPH_FILE.name)
GRAPH_DICTIONARY = _file_.convertGraphFileIntoDictionaryGraphvizStyle(GRAPH_FILE)
GRAPH = _graph_.Graph(GRAPH_DICTIONARY, 2)
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

def createCycleGraph(edges, vertices, name):
    
    newEdgesCollection = edges  
    maxV = int(max(vertices))
    vertices.append(str(maxV + 1))
    newMaxV = int(max(vertices))
    
    for v in vertices:
        if int(v) != int(newMaxV):
            edge = str(v) + GRAPH_EDGE_SEPARATOR + str(newMaxV)
            newEdgesCollection.append(edge)
    
    edgesDictionary = {}
    edgesDictionary['name'] = name
    newEdgesTab = []
    
    for edge in newEdgesCollection:
        text = edge.split(GRAPH_EDGE_SEPARATOR) 
        newEdgesTab.append(text)
        
    edgesDictionary['name'] = name
    edgesDictionary['edges'] = newEdgesTab
    edgesDictionary['vertices'] = vertices
    
    return edgesDictionary

def createCyclicGraph(edges, vertices, name):
    
    newEdgesCollection = edges  
    
    edgesDictionary = {}
    edgesDictionary['name'] = name
    newEdgesTab = []
    
    for edge in newEdgesCollection:
        text = edge.split(GRAPH_EDGE_SEPARATOR) 
        newEdgesTab.append(text)
        
    edgesDictionary['name'] = name
    edgesDictionary['edges'] = newEdgesTab
    edgesDictionary['vertices'] = vertices
    
    return edgesDictionary

def createCyclicGraphFile(circleGraph):
    file_path = "F:\GitHub\GiSwI\_model_\_files\_lists_"  
    _file_.createGraphFile(file_path, circleGraph['name'], circleGraph['edges'])
    

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
    
    edges = edges_dictionary(GRAPH.getEdgesCollection(), GRAPH.getUniqueVertices())
    
    build_array(_description, "\n\nWierzcholki, ich polaczenia oraz stopnie:")
    for i in sorted(edges):
        build_array(_description, "\n")
        build_array(_description, str(i))
        build_array(_description, ": ")
        build_array(_description, str(edges.get(i)))
        
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
    
    edges = edges_dictionary(GRAPH.getEdgesCollection(), GRAPH.getUniqueVertices())
    
    minV = int(min(GRAPH.getUniqueVertices()))
    maxV = int(max(GRAPH.getUniqueVertices()))
    list1 = list(dfs_paths(edges, minV, maxV))
    
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
    
    edgeCheck1 = str(maxPath[0]) + GRAPH_EDGE_SEPARATOR + str(maxPath[-1])
    edgeCheck2 = str(maxPath[-1]) + GRAPH_EDGE_SEPARATOR + str(maxPath[0])
    
    build_array(_description, "\nGraf ")
    build_array(_description, GRAPH.getName())
    build_array(_description, " jest grafem ") 
    
    if (edgeCheck1 or edgeCheck2) in GRAPH.getEdgesCollection():
        if maxPath[-2] != minV:
            build_array(_description, "cyklicznym wedlug sciezki: ")
            build_array(_description, str(maxPath))
            build_array(_description, ", zaczynajac od wierzcholka ")
            build_array(_description, str(minV))
            build_array(_description, " do wierzcholka ")
            build_array(_description, str(maxV))
            build_array(_description, ", miedzy ktorymi rowniez istnieje polaczenie zamykajace cykl.\n")
            
            circleGraph = createCycleGraph(GRAPH.getEdgesCollection(), GRAPH.getUniqueVertices(), "W")
            createCyclicGraphFile(circleGraph)
            
            build_array(_description, "\nLista krawedzi grafu typu kolo W: \n")
            
            for i in circleGraph['edges']:
                build_array(_description, str(i).replace("['", "").replace("']", "").replace("', '", " -- "))
                build_array(_description, "\n")
    else:
        build_array(_description, "acyklicznym gdyz brak polaczenia zamykajacego cykl od wierzcholka ")  
        build_array(_description, str(minV))
        build_array(_description, " do wierzcholka ")
        build_array(_description, str(maxV)) 
        build_array(_description, ".")
    

    result = result.join(_description)
    
    return result 

def task_three():
    GRAPH_FILE_PATH = "F:\GitHub\GiSwI\_model_\_files\_lists_\w.txt"
    GRAPH_FILE_MODE = 'r'
    GRAPH_FILE = _file_.readWriteFile(GRAPH_FILE_PATH, GRAPH_FILE_MODE)
    FILE_DESCRIPTION = "Plik uzyty do wczytania grafu: " + str(GRAPH_FILE.name)
    GRAPH_DICTIONARY = _file_.convertGraphFileIntoDictionaryGraphvizStyle(GRAPH_FILE)
    GRAPH = _graph_.Graph(GRAPH_DICTIONARY, 2)
    GRAPH_EDGE_SEPARATOR = GRAPH.GRAPH_EDGE_SEPARATOR
    
    result = ""    
    _description = []
    
    build_array(_description, FILE_DESCRIPTION) 
    build_array(_description, "\n") 

    edges = edges_dictionary(GRAPH.getEdgesCollection(), GRAPH.getUniqueVertices())
    
    build_array(_description, "\nWierzcholki i krawedzie, majace polaczenie z wszystkimi innymi wierzcholkami: ")
    allFullEdges = {}
    for i in edges:
        count = 0
        
        if len(edges.get(i)) == (len(GRAPH.getUniqueVertices()) - 1):
            for j in GRAPH.getUniqueVertices():
                if int(j) in edges.get(i):
                    count += 1
            
            if count == (len(GRAPH.getUniqueVertices()) - 1):
                allFullEdges[i] = edges.get(i)
                build_array(_description, "\nWierzcholek: ")
                build_array(_description, str(i))
                build_array(_description, ", Krawedzie: ")
                build_array(_description, str(allFullEdges[i]))
         
    maxVerticeToRemove = max(allFullEdges)
    del edges[maxVerticeToRemove]
    for i in edges.values():
        i.remove(maxVerticeToRemove)
        
    build_array(_description, "\n\nWybrano do usuniecia wierzcholek: ")
    build_array(_description, str(maxVerticeToRemove))
    build_array(_description, " gdyz jest najwiekszy.")
    
    newCollection = []
    for i in GRAPH.getEdgesCollection():
        first = int(i[0])
        second = int(i[-1])
        
        if (first != maxVerticeToRemove) and (second != maxVerticeToRemove):
            newCollection.append(i)
            
    newUniqueVertices = []
    for i in newCollection:
        s = i.split(GRAPH_EDGE_SEPARATOR)
        
        first = s[0]
        second = s[1]
        
        if first not in newUniqueVertices:
            newUniqueVertices.append(first)
        if second not in newUniqueVertices:
            newUniqueVertices.append(second)
    
    cycliGraphName = "c"    
    cyclicGraph = createCyclicGraph(newCollection, newUniqueVertices, cycliGraphName)
    createCyclicGraphFile(cyclicGraph)
    
    build_array(_description, "\nPo usunieciu wierzcholka, zostal utworzony na jego podstawie graf cykliczny ")
    build_array(_description, cycliGraphName.upper())
    build_array(_description, " o krawedziach: \n")
    for i in newCollection:
        build_array(_description, str(i))
        build_array(_description, "\n")
    
    
    result = result.join(_description)
    
    return result 

def task_five():
    result = ""
    _description = []
    
    build_array(_description, FILE_DESCRIPTION) 
    build_array(_description, "\n") 
    
    edges = edges_dictionary(GRAPH.getEdgesCollection(), GRAPH.getUniqueVertices())
    
    # Graf jest spojny, jesli dla kazdych dwoch jego wierzcholkow istnieje sciezka, ktore je ze soba laczy
    connectedGraph = {}  # Graf spojny slownik
    count = 0  # Licznik wszystkich sciezek
    
    for i in GRAPH.getUniqueVertices():  # Dla kazdego wierzcholka sprawdz:
        uniqueVertices = GRAPH.getUniqueVertices()  # Wszystkie wierzcholki
        uniqueVertices.remove(i)  # ...oprocz sprawdzanego
        
        for u in uniqueVertices:  # Dla kazdego pozostalego weirzcholka
            # 1-2
            pathList = list(dfs_paths(edges, int(i), int(u)))  # Sprawdz wszystkie sciezki
            if len(pathList) > 0:  # Jesli istnieje sciezka
                s = str(i) + " -- " + str(u)
                connectedGraph[s] = pathList
                count += 1
            # 2-1
            pathList = list(dfs_paths(edges, int(u), int(i)))
            if len(pathList) > 0:
                s = str(u) + " -- " + str(i)
                connectedGraph[s] = pathList
                count += 1
            
    neededPaths = len(GRAPH.getUniqueVertices()) * (len(GRAPH.getUniqueVertices()) - 1)  # Potrzebna ilosc sciezek do grafu spojnego (kazdy z kazdym)     
    
    build_array(_description, "\nCzy graf ") 
    build_array(_description, GRAPH.getName()) 
    build_array(_description, " jest grafem spojnym? Aby nim byl musi posiadac sciezke miedzy wszystkimi wierzcholkami, czyli musi istniec minimum ") 
    build_array(_description, str(neededPaths)) 
    build_array(_description, " sciezek.") 
    
    count = 0  # Wszystkei sciezki
    count_full_path = 0  # Wszystkie pelne sciezki
    for i in sorted(connectedGraph):
        count += len(connectedGraph.get(i))  # Dodaj kazda sciezke
        
        for p in connectedGraph.get(i):
            if len(p) == (len(GRAPH.getUniqueVertices())):  # Dodaj pelne sciezki
                count_full_path += 1
        
    build_array(_description, "\nLiczba istniejacych wszystkich sciezek: ")  
    build_array(_description, str(count))    
    build_array(_description, "\nLiczba istniejacych pelnych sciezek przez kazdy wierzcholek(Cykl Eulera): ")  
    build_array(_description, str(count_full_path)) 
    build_array(_description, "\n\nWszystkie dostepne sciezki: \n")    

    if count_full_path >= neededPaths:  # Jesli liczba sciezek jest >= od wymaganych
        for i in sorted(connectedGraph):
            build_array(_description, str(i))  
            build_array(_description, ": ") 
            build_array(_description, str(connectedGraph.get(i))) 
            build_array(_description, "\n")
    
        dictionary = graph_degree(
            GRAPH.getEdgesCollection(), int(len(GRAPH.getUniqueVertices()))
        )
        
        build_array(_description, "\nAby graf spojny byl grafem Eulerowskim, stopien kazdego jego wierzcholek musi byc liczba parzysta.\nStopnie wierzcholkow: ")
        for i in sorted(edges):
            build_array(_description, "\n")
            build_array(_description, str(i))
            build_array(_description, ": ")
            build_array(_description, str(edges.get(i)))
        
            for j in dictionary.keys():
                if i == j:
                    build_array(_description, ", Stopien wierzcholka: det(")
                    build_array(_description, str(j))
                    build_array(_description, ") = ")
                    build_array(_description, str(dictionary.get(j)))
        
        degree_count = 0  # Liczba stopni parzystych
        degree_count_odd = 0  # Liczba stopni nieparzystych
        for i in dictionary.keys():
            if i % 2 == 0:
                degree_count += 1
            else:
                degree_count_odd += 1
        
        if degree_count == int(len(GRAPH.getUniqueVertices())):  # Czy wszystkei stopnie sa parzyste
            build_array(_description, "\n\nStopnie wszystkich wierzcholkow grafu ")
            build_array(_description, GRAPH.getName())
            build_array(_description, " sa liczbami parzystymi, wiec jest on Grafem Eulerowskim.")
        elif degree_count_odd == 2:  # Czy dokladnie 2 stopnie sa nieparzyste
            build_array(_description, "\n\nGraf ")
            build_array(_description, GRAPH.getName())
            build_array(_description, " posiada 2 wierzcholki, ktorych stopien jest liczba nieparzysta co czyni go Grafem Poleulerowskim.")
        else:
            build_array(_description, "\n\nGraf ")
            build_array(_description, GRAPH.getName())
            build_array(_description, " jest Grafem Nieeulerowskim.")
    else:
        build_array(_description, "\n\nGraf ")
        build_array(_description, GRAPH.getName())
        build_array(_description, " jest Grafem Nieeulerowskim.")


    result = result.join(_description)
    
    return result


print(task_five())