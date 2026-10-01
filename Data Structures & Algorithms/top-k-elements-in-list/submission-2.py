class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]


        for num, frequency in count.items():
            buckets[frequency].append(num)
        
        result = []
        
        for index in range(len(buckets) -1, -1, -1):
            for num in buckets[index]:
                result.append(num)
                if len(result) == k:
                    return result
        