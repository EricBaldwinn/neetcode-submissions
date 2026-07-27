class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        upper = max(piles)
        lower = 1
        best = upper

        while lower <= upper:
            speed = (upper + lower) // 2
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
            
            if hours <= h:
                best = speed
                upper = speed - 1
            else:
                lower = speed + 1
        
        return best
            


