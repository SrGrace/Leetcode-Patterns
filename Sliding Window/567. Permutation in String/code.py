class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        a1, a2 = [0]*26, [0]*26
        for x in s1:
            a1[ord(x) - ord('a')] += 1
        
        for i in range(len(s2)):
            a2[ord(s2[i]) - ord('a')] += 1
            
            if i >= len(s1):
                a2[ord(s2[i-len(s1)]) - ord('a')] -= 1
                
            if a1 == a2:
                return True
            
        return False
    
