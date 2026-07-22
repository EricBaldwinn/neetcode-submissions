class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window with char count
        window = [0] * 26
        need = [0] * 26

        for char in s1:
            index = ord(char) - ord("a")
            need[index] += 1
        
        left = 0

        for right in range(len(s2)):
            char = s2[right]
            index = ord(char) - ord("a")
            window[index] += 1

            while right - left + 1 > len(s1):
                leftindex = ord(s2[left]) - ord("a")
                window[leftindex] -= 1
                left += 1
            
            if window == need:
                return True
        
        return False
        