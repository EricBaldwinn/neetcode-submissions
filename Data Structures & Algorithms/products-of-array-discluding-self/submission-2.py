class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        prefix = 1

        for index in range(len(nums)):
            currentNum = nums[index]
            answer[index] = prefix
            prefix *= currentNum
        
        suffix = 1

        for index in range(len(nums) - 1, -1, -1):
            answer[index] *= suffix
            suffix *= nums[index]
        
        return answer
            
        