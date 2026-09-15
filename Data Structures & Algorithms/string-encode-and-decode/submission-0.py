class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for word in strs:
            string += str(len(word)) + "#" + str(word)
        
        return string

    def decode(self, s: str) -> List[str]:
        decodedArray = []

        i = 0
        while i < len(s):
            num = ""
            word = ""
            while s[i] != "#":
                num += s[i]
                i += 1
            i += 1
            for j in range(i, i + int(num)):
                word += s[j]
                i += 1
            decodedArray.append(word)

        return decodedArray


            
