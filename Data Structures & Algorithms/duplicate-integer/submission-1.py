class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        window = set()
        left = 0

        for right in range(len(nums)):
            currentnum = nums[right]
            if currentnum in window:
                return True
            
            window.add(currentnum)
        
        return False