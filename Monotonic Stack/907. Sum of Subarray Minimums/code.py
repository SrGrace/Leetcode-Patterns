class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        stack = []
        result = [0]*(n+1)

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            j = stack[-1] if stack else -1
            result[i] = result[j] + (i-j)*arr[i]
            stack.append(i)
            # print("stack: ", stack)
            # print("result: ", result)
        
        return sum(result) % 1000000007

  # explanation: https://leetcode.com/problems/sum-of-subarray-minimums/solutions/257811/python-on-slightly-easier-to-grasp-solut-80xm
