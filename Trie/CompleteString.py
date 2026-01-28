# Longest string which contains all prefixes in the Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True
    
    def checkAllPrefixes(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            if not node.isEnd:
                return False
        return True
    
    def longestCompleteString(self,n,a) -> str:
        trie = Trie()
        for word in a:
            trie.insert(word)
        
        longest = ""
        for word in a:
            if trie.checkAllPrefixes(word):
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word
        
        return longest if longest else "None"