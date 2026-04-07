class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash_map = {}
        sub_sum, max_l = 0, 0

        for i, n in enumerate(nums):
            if n == 1:
                sub_sum += 1
            else:
                sub_sum -= 1

            if sub_sum == 0:
                max_l = i + 1 
            elif sub_sum in hash_map:
                max_l = max(max_l, i - hash_map[sub_sum])
            else:
                hash_map[sub_sum] = i
        
        return max_l # O(n), O(n)
            
