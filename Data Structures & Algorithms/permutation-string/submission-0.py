from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Hash = Counter(s1)
        lengthS1 = len(s1)

        for r in range(lengthS1 - 1, len(s2)):
            if Counter(s2[r - lengthS1 + 1:r + 1]) == s1Hash:
                return True

        return False