class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

# Trie contains methods to insert, search, and delete words
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # Insert word into trie
    def insert(self,word:str)->None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isEnd = True
    # Search word in trie
    def search(self,word:str)-> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.isEnd
    
    # Search for prefix
    def startsWith(self, prefix:str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True




trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("app"))
print(trie.startsWith("ap"))

# TC O(L) where L is the length of the word
# SC O(1) for search and startsWith, O(L) for insert in worst




