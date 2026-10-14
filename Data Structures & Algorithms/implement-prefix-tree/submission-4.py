class TrieNode:
    def __init__(self, children = {}, isEnd = False):
        self.children = children
        self.isEnd = isEnd

class PrefixTree:

    def __init__(self):
        self.head = TrieNode({})
        

    def insert(self, word: str) -> None:
        i = 0
        curr = self.head
        while i < len(word) and word[i] in curr.children:
            curr = curr.children[word[i]]
            i += 1
        
        while i < len(word):
            curr.children[word[i]] = TrieNode({})
            curr = curr.children[word[i]]
            i += 1

        curr.isEnd = True
        
    def search(self, word: str) -> bool:
        i = 0
        curr = self.head
        while i < len(word) and word[i] in curr.children:
            curr = curr.children[word[i]]
            i += 1
        
        return i == len(word) and curr.isEnd == True
        

    def startsWith(self, prefix: str) -> bool:
        i = 0
        curr = self.head
        while i < len(prefix) and prefix[i] in curr.children:
            curr = curr.children[prefix[i]]
            i += 1
        
        return i == len(prefix)

        
        