class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            hours = 0

            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours > h:
                left = mid + 1
            else:
                right = mid - 1
        
        return left


        