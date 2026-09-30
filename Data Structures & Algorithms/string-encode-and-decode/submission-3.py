class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstr = ""
        delimiter = "$"
        for word in strs:
            totalchars = len(word)
            encodedstr += str(totalchars) + delimiter + word
        
        return encodedstr



    def decode(self, s: str) -> List[str]:
        # iterate over str
        # find instance of digits with delimiter behind them
        # based on digits and delimiter index use digits to get first string 
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "$":
                j += 1

            length = int(s[i:j])
            word = s[j + 1:j + 1 + length]
            result.append(word)

            i = j + 1 + length

        return result
        
