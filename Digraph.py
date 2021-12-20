from collections import defaultdict
from typing import List
from Graph import Graph

class Digraph(Graph):
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

