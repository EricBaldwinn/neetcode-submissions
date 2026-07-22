class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # char count with sliding window
        window = [0] * 26
        count = 0

        left = 0
        for right in range(len(s)):
            char = s[right]
            index = ord(char) - ord("A")
            window[index] += 1

            while max(window) + k < (right - left + 1):
                leftindex = ord(s[left]) - ord("A")
                window[leftindex] -= 1
                left += 1
            
            count = max(count, right - left + 1)
        
        return count
