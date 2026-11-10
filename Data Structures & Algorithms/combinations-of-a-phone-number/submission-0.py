class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        
        numToLetters = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"],
        }

        output = []

        def backtrack(start, path):
            if start == len(digits):
                output.append("".join(path[:]))
                return
            
            for ch in numToLetters[digits[start]]:
                path.append(ch)
                backtrack(start + 1, path)
                path.pop()
        
        backtrack(0, [])
        return output

