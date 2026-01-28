# Implementing Trie 2

class TrieNode:
    def __init__(self):
        self.children = {}
        self.countPrefix = 0
        self.countEndWith = 0
    
class Trie: 
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.countPrefix += 1
        node.countEndWith += 1
    
    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.countEndWith
    
    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.countPrefix
    
    def erase(self, word: str) -> None:
        node = self.root
        stack = []
        for char in word:
            if char not in node.children:
                return  # Word not found, nothing to erase
            stack.append((node, char))
            node = node.children[char]
        
        if node.countEndWith > 0:
            node.countEndWith -= 1
            for parent, char in reversed(stack):
                child = parent.children[char]
                child.countPrefix -= 1
                if child.countPrefix == 0:
                    del parent.children[char]
                else:
                    break