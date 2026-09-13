from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            sortedKey = tuple(sorted(string))

            groups[sortedKey].append(string)

        return list(groups.values())