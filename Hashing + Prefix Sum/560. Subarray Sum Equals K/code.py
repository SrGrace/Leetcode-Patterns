class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = {0:1}
        count = 0
        sub_sum = 0
      
        for n in nums:
            sub_sum += n
            if sub_sum - k in hash_map:
                count += hash_map[sub_sum - k]
              
            hash_map[sub_sum] = hash_map.get(sub_sum, 0) + 1
          
        return count # O(n), O(n)
      
