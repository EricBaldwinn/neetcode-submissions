class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # signals non-decreasing order, O(1) space
        # pattern two pointers
        # brute force loop through every number record them in hashmap or set and then find complament
        left = 0
        right = len(numbers) - 1

        for idx in range(len(numbers)):
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

            
        
        return []
        