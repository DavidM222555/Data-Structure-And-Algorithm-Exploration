

# A trie is a data structure that has applications in things like 
# autocomplete where it can be used to generate the possible completions
# of a given prefix (some start of a string)
# 
# Tries effectively treat each letter a node in a tree where the leaves
# of a tree represent words in the structure. Given these properties we can 
# define certain functions using a Trie that given a particular prefix return 
# all possible endings of that string, which sounds very similar to the idea of auto-complete. 
# Furthermore, in that same vein we can use the fact that we have a value associated with each node that 
# can provide us a certain weight to each word and allow us to rank words based off how common they are, allowing us
# to provide better auto-complete suggestions.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value : str = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    
    def insert_helper(self, node_to_insert_at, string_to_insert, value):
        for char in string_to_insert: # This loop traverses the tree character by character and directs node_to_insert_at to a leaf it will take
            if(char not in node_to_insert_at.children):
                node_to_insert_at.children[char] = TrieNode()
            
            node_to_insert_at = node_to_insert_at.children[char]

        node_to_insert_at.value = value # Give it an associated value passed by the user. Could potentially be used for ranking purposes or some other form of auxiliary data

    def insert(self, string_to_insert, value):
        self.insert_helper(self.root, string_to_insert, value)


testTrie = Trie()
testTrie.insert("abc", "3")
testTrie.insert("acd", "4")
testTrie.insert("bcd", "5")
print(testTrie.root.children)

