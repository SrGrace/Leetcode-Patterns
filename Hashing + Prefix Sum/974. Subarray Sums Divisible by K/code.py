class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref_sum = 0
        count = 0
        hash_map = {0:1}

        for n in nums:
            pref_sum += n

            remainder = pref_sum % k
            if remainder in hash_map:
                count += hash_map[remainder]

            hash_map[remainder] = hash_map.get(remainder, 0) + 1
        
        return count # O(n), O(n)
