class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary serach but need to do binary search on each half of the initial mid

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (right + left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]

            # need to find what side is still sorted
        