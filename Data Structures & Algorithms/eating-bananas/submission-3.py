class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            eatingspd = (right + left) // 2
            hours = 0
            for pile in piles:
                hours += ((pile + eatingspd - 1) // eatingspd)
            
            if hours <= h:
                result = eatingspd
                right = eatingspd - 1
            else:
                left = eatingspd + 1
        
        return result

        