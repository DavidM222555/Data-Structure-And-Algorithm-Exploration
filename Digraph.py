from collections import defaultdict
from typing import List

class Digraph():
    def __init__(self, list_of_vertices : List[str]):
        self.dict_for_vertices = defaultdict()

        for vertice in list_of_vertices:
            self.add_vertice(vertice)

    def add_edge(self, a : str, b : str):
        if(a not in self.dict_for_vertices.keys() or b not in self.dict_for_vertices.keys()):
            raise ValueError("At least one vertice is undefined")

        self.dict_for_vertices[a].append(b) 

    # Adds multiple edges at once in the form of [["A", "B"], ["C", "D"]]
    def add_edges(self, list_of_edges : List[List[str]]):
        for edge in list_of_edges:
            self.add_edge(edge[0], edge[1])


    # Adds an edge from a to b and b to a
    def add_dual_edge(self, a : str, b : str):
        if(a not in self.dict_for_vertices.keys() or b not in self.dict_for_vertices.keys()):
            raise ValueError("At least one vertice is undefined")
        
        self.add_edge(a, b)
        self.add_edge(b, a)

    def add_vertice(self, vertice_name : str):
        if(vertice_name in self.dict_for_vertices.keys()):
            raise ValueError("Vertice already in graph")

        self.dict_for_vertices[vertice_name] = []

    def get_neighbors(self, vertice_name : str):
        if(vertice_name not in self.dict_for_vertices.keys()):
            raise ValueError("Vertice not in graph")

        return self.dict_for_vertices[vertice_name]

    # Returns all vertices in the graph
    def get_vertices(self):
        return self.dict_for_vertices.keys()

    def print_vertices(self):
        for vertice in self.dict_for_vertices.keys():
            print(vertice, " ", self.dict_for_vertices[vertice])