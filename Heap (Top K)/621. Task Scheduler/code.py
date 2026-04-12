class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """

        Each occurrence of task X takes one CPU cycle. 
        There are (maxCountX - 1) scheduled occurrences, and between each two consecutive occurrences, there are at least N CPU cycles.

        Therefore, the total CPU cycles can be calculated as follows:

        TotalCPUcycles=(maxCountX−1)⋅(N+1)

        """
        freq = [0]*26
        max_count = 0

        for task in tasks:
            freq[ord(task) - ord("A")] += 1
            max_count = max(max_count, freq[ord(task) - ord("A")])
        
        time = (max_count - 1)*(n+1)
        for f in freq:
            if max_count == f:
                time += 1
        
        return max(len(tasks), time) # O(N+26) = O(N), O(26) = O(1)
