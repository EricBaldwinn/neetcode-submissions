class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        prev = {}

        for right in range(len(nums)):
            currentnum = nums[right]
            if currentnum not in prev:
                prev[currentnum] = right
            
            complament = target - currentnum

            if complament in prev and prev[complament] != right:
                return [prev[complament], right]
        
        return []