class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            l, r = i+1, n-1
            remain = -nums[i]
            while l < r:
                if nums[l] + nums[r] == remain:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > remain:
                    r -= 1
                else:
                    l += 1
        return ans
                
        
        
