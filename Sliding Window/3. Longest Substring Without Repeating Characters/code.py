class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## Approach 2 - set
        seen = set()
        left, max_len = 0, 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right-left+1)

        return max_len # o(n), o(min(n, charset(26)))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## Approach 1 - hash map
        cache = dict()
        res, last_match = 0, -1
        for i, char in enumerate(s):
            if char in cache and last_match < cache[char]:
                last_match = cache[char]
            res = max(res, i-last_match)
            cache[char] = i
        
        return res # O(n), O(n)
