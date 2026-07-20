class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        need = [0] * 26
        for char in s:
            index = ord(char) - ord("a")
            need[index] += 1
        
        charcount = [0] * 26
        for char in t:
            index = ord(char) - ord("a")
            charcount[index] += 1
        
        if need == charcount:
            return True
        
        return False