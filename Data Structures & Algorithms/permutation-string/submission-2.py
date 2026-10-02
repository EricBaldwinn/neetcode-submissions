class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needed = [0] * 26

        for char in s1:
            index = ord(char) - ord("a")
            needed[index] += 1
        
        left = 0
        currentCount = [0] * 26
        
        for right in range(len(s2)):
            char = s2[right]
            index = ord(char) - ord('a')
            currentCount[index] += 1

            while right - left + 1 > len(s1):
                leftindex = ord(s2[left]) - ord("a")
                currentCount[leftindex] -= 1
                left += 1
            
            if needed == currentCount:
                return True
        
        return False

