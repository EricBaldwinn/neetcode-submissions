class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, frequency in count.items():
            buckets[frequency].append(num)

        for frequency in range(len(nums), 0, -1):
            for num in buckets[frequency]:
                result.append(num)
            if len(result) == k:
                return result
        