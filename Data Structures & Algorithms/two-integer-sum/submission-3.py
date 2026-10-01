class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index in range(len(nums)):
            num = nums[index]

            diff = target - num

            if diff in seen:
                return [seen[diff], index]
            
            seen[num] = seen.get(num, index)
        
        
        