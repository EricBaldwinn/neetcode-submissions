class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # keep a count dict of whats needed of s1

        # iterate over s2 when char in s1 check if permutation by using len of s1 and comparing count
        needed = {}
        window = {}

        for char in s1:
            needed[char] = needed.get(char, 0) + 1
        
        left = 0
        for right in range(len(s2)):
            char = s2[right]
            window[char] = window.get(char, 0) + 1
            if (right - left + 1) > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            
            if needed == window:
                return True
        
        return False
