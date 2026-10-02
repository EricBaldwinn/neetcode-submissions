class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        longest = 0
        left = 0

        for index in range(len(s)):
            char = s[index]
            countindex = ord(char) - ord("A")
            count[countindex] += 1

            while (index - left + 1) - max(count) > k:
                leftindex = ord(s[left]) - ord("A")
                count[leftindex] -= 1
                left += 1
            
            longest = max(longest, index - left + 1)
        
        return longest
        