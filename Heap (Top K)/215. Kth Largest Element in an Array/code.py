class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1st approach - min heap
        import heapq

        heapq.heapify(nums) # min heap - O(n)
        print("stage1: ", nums)
        for _ in range(len(nums) - k): # O(n + (n-k)logn)
            heapq.heappop(nums)
            print("stage2: ", nums)
        print("stage_final: ", nums)
        return nums[0] # O(n + (n-k)logn)

        # 2nd approach - numpy
        import numpy as np
        return int(np.partition(nums, len(nums) - k)[len(nums) - k])

        # 3rd approach - max heap
        import heapq
        max_heap = [-a for a in nums] # O(n)
        heapq.heapify(max_heap)
        
        result = []
        for _ in range(k):
            result.append(-heapq.heappop(max_heap))
        
        return result[0] # O(n + Blogn)

