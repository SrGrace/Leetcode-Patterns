class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start, end = 0, len(people)-1
        boats = 0
        while start <= end:
            # 1 heavy + 1 light
            if people[start] + people[end] <= limit:
                start += 1
                end -= 1
            # heavy go alone
            else:
                end -= 1
            boats += 1
        
        return boats
