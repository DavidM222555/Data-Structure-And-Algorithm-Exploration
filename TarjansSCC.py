from collections import defaultdict
from typing import List

from Digraph import Digraph


# Tarjan's strongly connected component algorithm is a way for finding, in a directed graph,
# all vertices that are reachable from one another.
# The algorithm largely works by placing vertices on the stack in the order they are visited
# from a start node (by DFS). Items are removed from the stack only if their neighbors are also on the stack,
# otherwise we further recurse on the neighbors of a given vertice or if we are done fully with a component
# and don't have a path reachable to another vertex we just go to another vertex in the graph.
#
# Time complexity: O(|V| + |E|)
def Tarjans(G : Digraph):
    listOfComponents = list() # Stores each of the components in a unique list
    currentIndex = 0
    stack = list()

    stack = []
    indices = dict.fromkeys(G.get_vertices(), -1)
    lowValues = dict.fromkeys(G.get_vertices(), -1) # Used for storing the component a given indexed vertice belongs to.

    for vertice in G.get_vertices():
        if(indices[vertice] == -1): # Is the index undefined / -1?
            connect(G, vertice, indices, lowValues, stack, currentIndex, listOfComponents)

    return listOfComponents


# Helper function for Tarjan's.
# Implementation partly guided by psuedocode from https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm 
# with some minor changes to make it Python specific.
def connect(G : Digraph, vertex : str, indices : List[int], lowValues : List[int], stack : List[str], currentIndex : int, returnList: List[List]):
    indices[vertex] = currentIndex
    lowValues[vertex] = currentIndex

    currentIndex += 1
    stack.append(vertex)

    for neighbor in G.get_neighbors(vertex):
        if(indices[neighbor] == -1):
            connect(G, neighbor, indices, lowValues, stack, currentIndex, returnList)
            lowValues[vertex] = min(lowValues[vertex], lowValues[neighbor])
        elif(neighbor in stack):
            lowValues[vertex] = min(lowValues[vertex], indices[neighbor])

    # This tells us we can start building a component -- basically we have backtracked far enough to know we are at the initial
    # index of the 'root' of a strong component -- here root just means the lowest valued index of a node of a component.
    if(lowValues[vertex] == indices[vertex]):
        newComponent = list() 

        while(1): # Get the vertices that make up a component
            currentValue = stack.pop()

            newComponent.append(currentValue)

            if(currentValue == vertex): # We are done building this component once we have gotten the 'root' of the component from the stack
                break
        
        returnList.append(newComponent)


# Tests various cases for Tarjan's algorithm -- including but not limited to
# the empty graph, the graph of one vertice, graphs with multiple components, graphs of one component, 
# and graphs of multiple components with long paths amongst each other.
def TestsForTarjans():
    testsPassed = True

    EmptyGraph = Digraph([])
    GraphWithOneVertice = Digraph(["A"])

    GraphWithMultipleComponents = Digraph(["A", "B", "C", "D", "E"])
    GraphWithMultipleComponents.add_dual_edge("A", "B") # Defines a component
    GraphWithMultipleComponents.add_dual_edge("C", "D") # Defines a component
    GraphWithMultipleComponents.add_edge("E", "D") # Will be an isolated component but does have a connection to D
    ValidComponents = [["A", "B"], ["C", "D"], ["E"]]

    # Graph that contains a long path from left to right but only has one valid component
    GraphWithLongPath = Digraph(["A", "B", "C", "D", "E"])
    GraphWithLongPath.add_edge("A", "B")
    GraphWithLongPath.add_edge("B", "C")
    GraphWithLongPath.add_edge("C", "D")
    GraphWithLongPath.add_edge("D", "E") 
    GraphWithLongPath.add_edge("E", "D") # The only two node component in the graph will be D, E
    ValidComponentsForLongPath = [["A"], ["B"], ["C"], ["D", "E"]]


    if(Tarjans(EmptyGraph) != []):
        print("Test failed for empty graph")
        testsPassed = False

    if(Tarjans(GraphWithOneVertice) != [["A"]]):
        print("Test failed for graph with one vertice")
        testsPassed = False

    for component in Tarjans(GraphWithMultipleComponents):
        if(sorted(component) not in ValidComponents):
            print("Test failed for multiple components")
            testsPassed = False
    
    for component in Tarjans(GraphWithLongPath):
        if(sorted(component) not in ValidComponentsForLongPath):
            print("Test failed for graph with a long path but only one non-trivial component")
            testsPassed = False

    if(testsPassed):
        print("All tests passed.")


TestsForTarjans()