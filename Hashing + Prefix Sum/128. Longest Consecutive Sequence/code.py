class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_l = 0
        for x in nums:
            if x-1 not in nums:
                y = x+1
                while y in nums:
                    y += 1
                max_l = max(max_l, y-x)
        return max_l # O(n), O(n)
