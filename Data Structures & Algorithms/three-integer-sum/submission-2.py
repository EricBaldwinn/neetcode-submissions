class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for index in range(len(nums)):
            currennum = nums[index]
            if index > 0 and currennum == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                total = currennum + nums[left] + nums[right]

                if total == 0:
                    result.append([currennum, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result
        