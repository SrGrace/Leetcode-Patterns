class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bin_search(nums, target, searchFirst):
            l, r = 0, len(nums)-1
            res = -1
            while(l <= r):
                mid = l+(r-l)//2
                if nums[mid] == target:
                    res = mid
                    if searchFirst:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return res

        return [
            bin_search(nums, target, searchFirst=True),
            bin_search(nums, target, searchFirst=False)
        ]     
