from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.head

        i = 0
        while i < len(word) and word[i] in curr.children:
            curr = curr.children[word[i]]
            i += 1
        
        while i < len(word):
            curr.children[word[i]] = TrieNode()
            curr = curr.children[word[i]]
            i += 1
        
        curr.isEnd = True

    def search(self, word: str) -> bool:
        i = 0
        q = deque([self.head])

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                
                if word[i] in curr.children:
                    if word == "day": print("bruh", word[i], curr.children, curr.isEnd)
                    q.append(curr.children[word[i]])
                    
                
                elif word[i] == ".":
                    for node in curr.children:
                        q.append(curr.children[node])

            i += 1
            if i == len(word): break

        for node in q:
            if node.isEnd:
                return i == len(word)

        return False