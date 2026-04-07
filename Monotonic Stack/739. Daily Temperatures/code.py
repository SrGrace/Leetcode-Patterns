class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        next_greater = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                last = stack.pop()
                next_greater[last] = idx - last

            stack.append(idx)

        return next_greater # O(n), O(n)
