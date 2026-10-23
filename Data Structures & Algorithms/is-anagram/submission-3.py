class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        needed = [0] * 26

        for char in s:
            index = ord(char) - ord("a")
            needed[index] += 1
        
        current_count = [0] * 26

        for char in t:
            index = ord(char) - ord("a")
            current_count[index] += 1
        
        return current_count == needed
            