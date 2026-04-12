class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq

        minheap = []
        result = []

        m, n = len(matrix), len(matrix[0])

        for i in range(m): # O(mlogm)
            if matrix[i]:
                heapq.heappush(minheap, (matrix[i][0], i, 0)) # val, arr_index, element_index
              
        print("stage 1: ", minheap)
        
        while minheap: # 
            val, arr_index, ele_index = heapq.heappop(minheap)
            result.append(val) # smallest element

            # If there is another element in the same array, push it to the heap
            if ele_index + 1 < n:
                next_val = matrix[arr_index][ele_index + 1]
                heapq.heappush(minheap, (next_val, arr_index, ele_index + 1))
              
            print("stage 2: ", minheap)

        print("result: ", result)
          
        return result[k-1] # O(n*mlogm), O(n*m)

"""
input: [[1,5,9],[10,11,13],[12,13,15]]

stage 1:  [(1, 0, 0), (10, 1, 0), (12, 2, 0)]
stage 2:  [(5, 0, 1), (12, 2, 0), (10, 1, 0)]
stage 2:  [(9, 0, 2), (12, 2, 0), (10, 1, 0)]
stage 2:  [(10, 1, 0), (12, 2, 0)]
stage 2:  [(11, 1, 1), (12, 2, 0)]
stage 2:  [(12, 2, 0), (13, 1, 2)]
stage 2:  [(13, 1, 2), (13, 2, 1)]
stage 2:  [(13, 2, 1)]
stage 2:  [(15, 2, 2)]
stage 2:  []

result: [1, 5, 9, 10, 11, 12, 13, 13, 15]
"""
