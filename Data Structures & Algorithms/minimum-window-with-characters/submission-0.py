class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        need = len(count_t)
        have = 0
        left = 0
        right = 0
        res_l = float('inf')

        count_s = defaultdict(int)

        l = 0
        for r in range(len(s)):
            count_s[s[r]] += 1
            if count_s[s[r]] == count_t[s[r]]: have += 1

            while have == need:
                if r - l + 1 < res_l:
                    right, left = r, l
                    res_l = r - l + 1
                count_s[s[l]] -= 1
                if count_s[s[l]] < count_t[s[l]]: have -= 1
                l += 1

        return s[left:right + 1] if res_l != float('inf') else ""