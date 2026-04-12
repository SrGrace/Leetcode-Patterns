class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0]) # O(nlogn)

        prev = intervals[0]

        for interval in intervals[1:]: # O(n)
            if interval[0] <= prev[1]: # start <= end 
                prev[1] = max(prev[1], interval[1])
            else: # start > end 
                merged.append(prev)
                prev = interval
        
        merged.append(prev)

        return merged # O(nlogn), O(n)
