class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            day, total = 1, 0
            for weight in weights:
                total += weight
                if total > capacity: # too heavy, wait for the next day
                    total = weight
                    day += 1
                    if day > days: # cannot ship within days
                        return False
            return True

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
