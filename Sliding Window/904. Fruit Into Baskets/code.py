class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, max_f = 0, 0
        hash_map = dict()
        for right in range(len(fruits)):
            # expand right
            hash_map[fruits[right]] = hash_map.get(fruits[right], 0) + 1

            # shrink left
            while len(hash_map) > 2:
                hash_map[fruits[left]] -= 1
                if hash_map[fruits[left]] == 0:
                    del hash_map[fruits[left]]
                left += 1

            max_f = max(max_f, right-left+1)
            
        return max_f
