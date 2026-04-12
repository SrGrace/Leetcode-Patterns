class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxheap, -num)
        maxheap_top = -heappop(self.maxheap)
        heappush(self.minheap, maxheap_top)

        # balancing act
        if len(self.minheap) > len(self.maxheap):
            minheap_top = heappop(self.minheap)
            heappush(self.maxheap, -minheap_top)

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (-self.maxheap[0] + self.minheap[0])/2
        else:
            return -self.maxheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
