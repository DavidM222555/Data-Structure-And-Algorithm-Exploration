from Digraph import Digraph
from Graph import Graph

class WeightedGraph(Graph):
    def add_edge(self, a : str, b : str, value : float):
        if(a not in self.dict_for_vertices.keys() or b not in self.dict_for_vertices.keys()):
            raise ValueError("At least one vertice is undefined")

        self.dict_for_vertices[a].append([b, value]) 
        self.dict_for_vertices[b].append([a, value]) 

    def get_edges(self):
        seen_edges = []
        return_edges = []

        for vertice in self.get_vertices():
            for neighbor_vertice in self.get_neighbors(vertice):
                edge_to_consider = sorted([vertice, neighbor_vertice[0]])
                possible_edge_to_append = [vertice, neighbor_vertice[0], neighbor_vertice[1]]

                if(edge_to_consider not in seen_edges):
                    seen_edges.append(edge_to_consider)
                    return_edges.append(possible_edge_to_append)

        return sorted(return_edges, key = lambda x : x[2])

