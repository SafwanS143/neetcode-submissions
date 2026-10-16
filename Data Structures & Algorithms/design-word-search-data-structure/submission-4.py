class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        
        curr.isEnd = True
    
    def dfs(self, node, word, i):
        if i == len(word): return node.isEnd
        if word[i] != "." and word[i] not in node.children: return False

        if word[i] != ".":
            return self.dfs(node.children[word[i]], word, i + 1)

        return any(self.dfs(child, word, i + 1) for child in node.children.values())

        return False
            

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)
        
