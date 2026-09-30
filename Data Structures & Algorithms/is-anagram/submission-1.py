class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        needed = [0] * 26

        for char in s:
            index = ord(char) - ord("a")
            needed[index] += 1
        
        count = [0] * 26

        for char in t:
            index = ord(char) - ord("a")
            count[index] += 1
        
        return needed == count
        