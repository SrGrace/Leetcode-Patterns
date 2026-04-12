class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        freq = Counter(nums) # O(n)

        maxheap = []
        for n, f in freq.items(): # O(nlogn)
            heapq.heappush(maxheap, (-f, n)) 
        
        result = []
        for _ in range(k): # O(klogn)
            result.append(heapq.heappop(maxheap)[1])
        
        return result # O(nlogn), O(n)
