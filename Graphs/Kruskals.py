from collections import defaultdict
from typing import List

from WeightedGraph import WeightedGraph
from DisjointSet import DisjointSet

# Kruskal's algorithm is a relatively simple algorithm for finding the minimum spanning tree (MST in code) of a weighted graph.
# 
# Kruskal's effectively works by starting with a list of the edges in a graph sorted in increasing order and taking the smallest 
# weighted edges that don't form a cycle (a loop). The way we guarantee we don't form a cycle with our current edges is by utilizing 
# a disjoint-set data structure that allows us to keep track of which vertices are and are not currently in our MST.
def Kruskals(G : WeightedGraph):
    MST = [] # A list containing the edges of the MST

    disjoint_set_for_vertices = DisjointSet()
    list_of_edges = G.get_edges() # get_edges returns the edges sorted so Kruskal's doesn't have to take care of it.

    # Iterate through the vertices in the graph and make each their own disjoint set
    for vertice in G.get_vertices():
        disjoint_set_for_vertices.make_set(vertice)

    # Now iterate through all the edges (in sorted order) and progressively add edges that don't form a cycle.
    # We can tell if a cycle is formed based off whether two members of the disjoint set have a common root -- which is discovered by
    # the find method of the disjoint-set data structure
    for edge in list_of_edges:
        if(disjoint_set_for_vertices.find(edge[0]) != disjoint_set_for_vertices.find(edge[1])):
            MST.append(edge)
            disjoint_set_for_vertices.merge(edge[0], edge[1])
    
    return MST
    

wg = WeightedGraph(["a", "b", "c"])
wg.add_edge("a", "b", 3)
wg.add_edge("c", "b", 55)
wg.add_edge("a", "c", 1)

