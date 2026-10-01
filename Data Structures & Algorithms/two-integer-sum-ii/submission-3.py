class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevNum = {}

        for i, num in enumerate(numbers):
            diff = target - num
            if diff in prevNum:
                return [prevNum[diff] + 1, i + 1]
            else:
                prevNum[num] = i
            

        