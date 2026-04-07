class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = dict() 
        left, max_f = 0, 0
        for right in range(len(s)):
            # expand right
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1
            # track
            max_f = max(max_f, hash_map[s[right]])
            # shrink left
            if (right-left+1) - max_f > k:
                hash_map[s[left]] -= 1
                left += 1
        return len(s) - left


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = dict() 
        left, max_len = 0, 0
        for right in range(len(s)):
            # expand right
            hash_map[s[right]] += 1
            # shrink left
            while (right-left+1) - max(hash_map.values()) > k:
                hash_map[s[left]] -= 1
                if hash_map[s[right]] == 0:
                    del hash_map[s[right]]
                
                left += 1
            
            max_len = max(max_len, right-left+1)
        
        return max_len

  
