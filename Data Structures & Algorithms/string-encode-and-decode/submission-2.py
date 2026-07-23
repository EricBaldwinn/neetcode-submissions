class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = "#"
        encodedstr = ""
        for word in strs:
            length = len(word)
            encodedstr += str(length) + delimiter + word
        
        return encodedstr

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            start = j + 1
            length = int(s[i:j])
            end = start + length

            output.append(s[start:end])

            i = end

        
        return output


