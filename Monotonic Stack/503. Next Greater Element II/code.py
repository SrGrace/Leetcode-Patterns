class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        next_greater = [-1] * n

        for i in range(2 * n): # twice the len to make it circular
            while stack and nums[stack[-1]] < nums[i % n]:
                next_greater[stack.pop()] = nums[i % n]

            if i < n:
                stack.append(i)
        
        return next_greater # O(n), O(n)
