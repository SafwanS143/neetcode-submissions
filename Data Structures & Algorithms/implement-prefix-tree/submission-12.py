class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        i = 0
        while word[i] in curr.children:
            curr = curr.children[word[i]]
            i += 1
            if i == len(word): break
        else:
            while i < len(word):
                curr.children[word[i]] = TrieNode()
                curr = curr.children[word[i]]
                i += 1
        
        curr.isEnd = True
       

    def _walk(self, s):
        curr = self.root
        for ch in s:
            if ch not in curr.children: return [False, curr]
            curr = curr.children[ch]
            
        return [True, curr]

        

    def search(self, word: str) -> bool:
        found, node = self._walk(word)
        return found and node.isEnd 
       

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix)[0]
        