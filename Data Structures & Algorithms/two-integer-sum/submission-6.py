class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index in range(len(nums)):
            diff = target - nums[index]

            if diff in seen:
                return [seen[diff], index]
            
            seen[nums[index]] = index
        
        