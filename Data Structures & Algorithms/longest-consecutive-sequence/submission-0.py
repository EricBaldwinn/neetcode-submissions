class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        numbers = set(nums)

        for num in numbers:
            if num - 1 not in numbers:
                length = 1

                while (num + length) in numbers:
                    length += 1
                
                best = max(best, length)
        
        return best



        