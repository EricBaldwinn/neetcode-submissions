class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstr = ""
        delimiter = "#"
        for word in strs:
            length = len(word)
            encodedstr += str(length) + delimiter + word
        
        return encodedstr

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = s[i:j]
            start = j + 1
            end = start + int(length)
            word = s[start: end]
            decoded.append(word)
            i = end
        
        return decoded