from collections import defaultdict
from typing import List

from Digraph import Digraph


# Tarjan's strongly connected component algorithm is a way for finding, in a directed graph,
# all vertices that are reachable from one another.
# The algorithm largely works by placing vertices on the stack in the order they are visited
# from a start node (by DFS). From there, items are removed from the stack only if their neighbors are also on the stack,
# otherwise we further recurse on the neighbors of a given vertice. If we are done fully with a component
# and don't have a path reachable to another vertex we just go to another vertex in the graph arbitrarily (lexicographically, for example)
#
# Time complexity: O(|V| + |E|)
def Tarjans(G : Digraph):
    list_of_components = list() # Stores each of the components in a unique list
    current_index = 0
    stack = list()

    stack = []
    indices = dict.fromkeys(G.get_vertices(), -1)
    low_values = dict.fromkeys(G.get_vertices(), -1) # Used for storing the component a given indexed vertice belongs to.

    for vertice in G.get_vertices():
        if(indices[vertice] == -1): # Is the index undefined / -1?
            connect(G, vertice, indices, low_values, stack, current_index, list_of_components)

    return list_of_components


# Helper function for Tarjan's.
# Implementation partly guided by psuedocode from https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm 
def connect(G : Digraph, vertex : str, indices : List[int], low_values : List[int], stack : List[str], current_index : int, return_list: List[List]):
    indices[vertex] = current_index
    low_values[vertex] = current_index

    current_index += 1
    stack.append(vertex)

    for neighbor in G.get_neighbors(vertex):
        if(indices[neighbor] == -1):
            connect(G, neighbor, indices, low_values, stack, current_index, return_list)
            low_values[vertex] = min(low_values[vertex], low_values[neighbor])
        elif(neighbor in stack):
            low_values[vertex] = min(low_values[vertex], indices[neighbor])

    # This tells us we can start building a component -- basically we have backtracked far enough to know we are at the initial
    # index of the 'root' of a strong component -- here root just means the lowest valued index of a node of a component.
    if(low_values[vertex] == indices[vertex]):
        newComponent = list() 

        while(1): # Get the vertices that make up a component
            currentValue = stack.pop()

            newComponent.append(currentValue)

            if(currentValue == vertex): # We are done building this component once we have gotten the 'root' of the component from the stack
                break
        
        return_list.append(newComponent)


# Tests various cases for Tarjan's algorithm -- including but not limited to
# the empty graph, the graph of one vertice, graphs with multiple components, graphs of one component, 
# and graphs of multiple components with long paths amongst each other.
def TestsForTarjans():
    tests_passed = True

    empty_graph = Digraph([])
    graph_with_one_vertice = Digraph(["A"])

    graph_with_multiple_components = Digraph(["A", "B", "C", "D", "E"])
    graph_with_multiple_components.add_dual_edge("A", "B") # Defines a component
    graph_with_multiple_components.add_dual_edge("C", "D") # Defines a component
    graph_with_multiple_components.add_edge("E", "D") # Will be an isolated component but does have a connection to D
    valid_components = [["A", "B"], ["C", "D"], ["E"]]

    # Graph that contains a long path from left to right but only has one valid component
    graph_with_long_path = Digraph(["A", "B", "C", "D", "E"])
    graph_with_long_path.add_edge("A", "B")
    graph_with_long_path.add_edge("B", "C")
    graph_with_long_path.add_edge("C", "D")
    graph_with_long_path.add_edge("D", "E") 
    graph_with_long_path.add_edge("E", "D") # The only two node component in the graph will be D, E
    valid_components_for_long_path = [["A"], ["B"], ["C"], ["D", "E"]]

    if(Tarjans(empty_graph) != []):
        print("Test failed for empty graph")
        tests_passed = False

    if(Tarjans(graph_with_one_vertice) != [["A"]]):
        print("Test failed for graph with one vertice")
        tests_passed = False

    for component in Tarjans(graph_with_multiple_components):
        if(sorted(component) not in valid_components):
            print("Test failed for multiple components")
            tests_passed = False
    
    for component in Tarjans(graph_with_long_path):
        if(sorted(component) not in valid_components_for_long_path):
            print("Test failed for graph with a long path but only one non-trivial component")
            tests_passed = False

    if(tests_passed):
        print("All tests passed.")


TestsForTarjans()