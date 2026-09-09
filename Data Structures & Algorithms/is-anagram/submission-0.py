class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        
        for char in s:
            if char not in seen:
                seen[char] = 0
            
            seen[char] += 1
        
        for char in t:
            if char not in seen:
                return False
            
            seen[char] -= 1
        
        if all(value == 0 for value in seen.values()):
            return True
        
        else:
            return False