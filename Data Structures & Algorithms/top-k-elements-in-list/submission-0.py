class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        charcount = {}


        for num in nums:
            if num not in charcount:
                charcount[num] = 1
            else:
                charcount[num] += 1
        
        heap = [[] for _ in range(len(nums) + 1)]

        for key, value in charcount.items():
            heap[value].append(key)
        
        result = []

        for freq in range(len(heap) - 1, 0, -1):
            for num in heap[freq]:
                result.append(num)

                if len(result) == k:
                    return result
        
