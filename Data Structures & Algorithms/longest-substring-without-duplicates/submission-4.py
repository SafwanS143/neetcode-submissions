

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longSubstring = 0
        seen = set()

        while r < len(s):

            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            r += 1
            
            longSubstring = max(longSubstring, r - l)
            

        return longSubstring