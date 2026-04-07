class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = defaultdict(lambda: -1)
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            
            stack.append(num)
        
        return [next_greater[num] for num in nums1] # O(n+m), O(m)

        """
nums1 = [3,1,2]
nums2 = [2,1,3]
result = [-1,3,3]
--------------------
nums2 = [2,1,3]
st = []

nums2 = [2,1,3]
         ↑
st = [2]

nums2 = [2,1,3]
           ↑
st = [2, 1]

nums2 = [2,1,3]
             ↑
st = [2,1]

{1:3}
st = [2]

{1:3, 2:3}
st = []

[ 3,1,2](= num1)
  ↓ ↓ ↓
[-1,3,3](= result)
        """
        
