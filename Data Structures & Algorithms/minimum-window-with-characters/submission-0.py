class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for char in t:
            if char not in need:
                need[char] = 1
            else:
                need[char] += 1
        
        window = {}
        formed = 0
        required = len(need)
        best_len = float("inf")
        best_start = 0

        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                formed += 1
            
            while formed == required:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_start = left

                leftchar = s[left]
                window[leftchar] -= 1
                
                if leftchar in need and window[leftchar] < need[leftchar]:
                    formed -= 1
            
                left += 1

        
        if best_len == float("inf"):
            return ""

        return s[best_start:best_start + best_len]
            

        