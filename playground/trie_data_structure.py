from collections import OrderedDict


class TrieNode:
    def __init__(self):
        # An OrderedDict where each key is a character, and the value is a TrieNode
        self.children: OrderedDict[str, TrieNode] = OrderedDict()
        # Indicates if the node is the end of a complete string
        self.is_end_of_string: bool = False


class Trie:
    def __init__(self):
        # The root of the trie is an empty node
        self.root: TrieNode = TrieNode()

    def insert(self, string: str) -> None:
        current: TrieNode = self.root
        # Iterate over each character in the string
        for char in string:
            # If the character is not in the current node's children, add it
            if char not in current.children:
                current.children[char] = TrieNode()
            # Move to the next node
            current = current.children[char]
        # Mark the end of the string
        current.is_end_of_string = True

    def search(self, string: str) -> bool:
        current: TrieNode = self.root
        # Iterate over each character in the string
        for char in string:
            # If the character is not present, the string is not in the trie
            if char not in current.children:
                return False
            # Move to the next node
            current = current.children[char]
        # Return True if we are at the end of a string
        return current.is_end_of_string

    def starts_with(self, prefix: str) -> bool:
        current: TrieNode = self.root
        # Iterate over each character in the prefix
        for char in prefix:
            # If the character is not present, the prefix is not in the trie
            if char not in current.children:
                return False
            # Move to the next node
            current = current.children[char]
        # If we successfully traversed the prefix, return True
        return True

    def collect_lexical_order(self) -> list[str]:
        # List to hold the results
        result: list[str] = []
        # Start DFS from the root node
        dfs(self.root, [], result)
        return result


def dfs(node: TrieNode, path: list[str], result: list[str]) -> None:
    # If the current node marks the end of a string, add the path to the result
    if node.is_end_of_string:
        result.append("".join(path))

    # Traverse children nodes in insertion order
    for char in node.children:
        path.append(char)  # Add character to path
        dfs(node.children[char], path, result)
        path.pop()  # Remove character after traversing


# Example Usage
trie = Trie()
# Inserting strings derived from integers
trie.insert("1")
trie.insert("10")
trie.insert("11")
trie.insert("12")
trie.insert("2")
trie.insert("20")
trie.insert("21")
trie.insert("3")
trie.insert("19")

# Collecting all numbers in lexical order
lexical_order = trie.collect_lexical_order()
print(lexical_order)
