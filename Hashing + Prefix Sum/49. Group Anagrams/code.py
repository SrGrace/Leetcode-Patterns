class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                """
                [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0] (= "eat")
                [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0] (= "tea")
                """
                count[ord(c) - ord('a')] += 1
            group[tuple(count)].append(s) # tuple is hashable, list is not; group all anagrams with the same key

        return list(group.values())
        
