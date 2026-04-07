class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed) -> bool:     
            return sum(math.ceil(pile/speed) for pile in piles) <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left  + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
