from typing import List
from WeightedGraph import WeightedGraph

import heapq # For priority queue

# @param G: G is weighted undirected graph
# @param source: Source is the name of a vertex in the graph that will be the basis for finding all shortest paths
def Dijkstra(G: WeightedGraph, source : str):
    distances = {source : 0} # Initalize the distance dictionary with distance 0 for the source
    prev = {} # Used for backtracking to get the solution path for a given source to vertex shortest path

    distance_priority_queue = []
 
    # Begin by iterating over all the vertices and adding them as a key to our distance and previous dictionaries.
    # We begin by initilizing the distance values to infinity and previous values to "null" -- by the time the program stops we will
    # also know if a node is unreachable from the source if it has a null for its previous entry or inifinity as its distance
    for vertice in G.get_vertices():
        if(vertice != source):
            distances[vertice] = float("inf")
            prev[vertice] = "null"

    # Add the source vertex to our priority queue -- each entry in the priority queue is of the form (distance, vertex) where distance acts 
    # as the priority.   
    #
    # There are two ways this can be done but this way allows us to use Python's heapq without having to implement a way of updating 
    # priorities. Other versions of the algorithm add all the items to the queue at the start and update them progressively as the 
    # algorithm runs. Both versions have the same asymptotic complexity
    heapq.heappush(distance_priority_queue, (distances[source], source))

    while(distance_priority_queue): # Pop from the heap until it is empty -- when it is empty we have fully exhausted updating some paths
        current_min = heapq.heappop(distance_priority_queue)[1] # This will be a tuple so we need to access the second value, the vertice name

        vertices_in_queue = [item[1] for item in distance_priority_queue] # Get all vertices currently in the priority queue

        for neighbor in G.get_neighbors(current_min): # Neighbor consists of the neighbor vertice name and the edge weight
            potential_distance = distances[current_min] + neighbor[1] # Get the current distance to current_min + the edge distance to the neighbor

            if(potential_distance < distances[neighbor[0]]): # Can we update the current distance to one of our neighbors utilizing current_min?
                distances[neighbor[0]] = potential_distance
                prev[neighbor[0]] = current_min

                if(neighbor[0] not in vertices_in_queue):
                    heapq.heappush(distance_priority_queue, (potential_distance, neighbor[0])) # Add the element to the priority queue

    return [distances, prev]

# Various tests for the above implementation of Dijkstra's algorithm
def DijkstraTests():
    graph_with_one_node = WeightedGraph(["0"])
    solution_for_graph_with_one_node = {'0': 0}

    if(Dijkstra(graph_with_one_node, "0")[0] != solution_for_graph_with_one_node):
        print("Failed test for graph with a single node")

    # This graph should show that the distance to 3 is infinity if "0", "1", or "2" 
    # is the source.
    graph_with_two_components = WeightedGraph(["0", "1", "2", "3"])
    graph_with_two_components.add_edge("0", "1", 33)
    graph_with_two_components.add_edge("1", "2", 12)
    graph_with_two_components.add_edge("0", "2", 3)

    solution_for_graph_with_two_components = {'0': 0, '1': 15, '2': 3, '3': float('inf')}

    if(Dijkstra(graph_with_two_components, "0")[0] != solution_for_graph_with_two_components):
        print("Failed test for graph with two components")


DijkstraTests()
