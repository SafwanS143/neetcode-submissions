from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Hash = Counter(s1)
        lengthS1 = len(s1)
        windowCount = Counter(s2[0:lengthS1])

        for r in range(lengthS1, len(s2)):

            if windowCount == s1Hash:
                return True

            windowCount[s2[r]] += 1
            windowCount[s2[r - lengthS1]] -= 1

        if windowCount == s1Hash:
            return True

        return False