from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = longSubstring = 0
        window = defaultdict(int)
        maxf = 0

        for r in range(len(s)):
            window[s[r]] += 1
            maxf = max(maxf, window[s[r]])
            
            while r - l + 1 - maxf > k:
                window[s[l]] -= 1
                l += 1

            longSubstring = max(longSubstring, r - l + 1)
        

        return longSubstring