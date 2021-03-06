from typing import List


# Influenced by the Wiki article: https://en.wikipedia.org/wiki/Disjoint-set_data_structure

class DisjointSetNode():
    def __init__(self, name : str):
        self.name = name


class DisjointSet():
    def __init__(self):
        self.list_of_node_names = []
        self.node_to_label_dict = {}
        self.label_to_node_dict = {}

    # Creates a new set with a DisjointSetNet(set_label) as the root node
    def make_set(self, set_label : str):
        if(set_label not in self.list_of_node_names):
            set_to_add = DisjointSetNode(set_label)

            set_to_add.parent = set_to_add
            set_to_add.rank = 0

            self.list_of_node_names.append(set_label)
            self.node_to_label_dict[set_to_add] = set_label
            self.label_to_node_dict[set_label] = set_to_add
    
    # Finds the root (and thus label) for a given label x in our disjoint-set
    def find(self, x : str):
        return self.find_helper(self.label_to_node_dict[x])

    def find_helper(self, x : str):
        if(x.parent == x):
            return x
        else:
            x.parent = self.find_helper(x.parent)
            return x.parent

    # Merges two disjoint-sets together by merging the two trees into one. The root of the tree is decided by which
    # has the larger rank
    def merge(self, x : str, y : str):
        root_of_x = self.find(x)
        root_of_y = self.find(y)

        if(root_of_x.rank > root_of_y.rank):
            root_of_y.parent = root_of_x
        elif(root_of_x.rank < root_of_y.rank):
            root_of_x.parent = root_of_y 
        elif(root_of_x != root_of_y): # The case where they have the same rank and are not the exact same node
            root_of_y.parent = root_of_x
            root_of_x.rank = root_of_x.rank + 1

testSet = DisjointSet()

testSet.make_set("A")
testSet.make_set("B")

testSet.merge("A", "B")
