class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            char = s[right]
            while char in current:
                current.remove(s[left])
                left += 1
            current.add(s[right])
            longest = max(longest, len(current))
        return longest

        
        
        