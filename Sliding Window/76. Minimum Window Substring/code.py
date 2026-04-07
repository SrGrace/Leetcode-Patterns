class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        hash_map = defaultdict(int) 

        # Populate the hash_map with the frequency of each character in t
        # Time Complexity: O(|T|) to iterate over string t, Space Complexity: O(|T|)
        for ch in t:
            hash_map[ch] += 1

        # Initialize counter to track the number of characters needed to form a valid window
        counter = len(t)

        # Initialize two pointers, begin and end, to represent the sliding window
        begin, end = 0, 0

        # Initialize d to store the length of the smallest valid window found so far
        # Set to infinity initially to handle the case where no valid window is found
        d = float('inf')

        # Initialize head to store the starting index of the smallest valid window
        head = 0

        # Slide the end pointer to expand the window
        # Time Complexity: O(|S|) - each character in s is processed at most twice (once by end and once by begin)
        while end < len(s):
            # If the current character at end is in t and needed for the window, decrement counter
            if hash_map[s[end]] > 0:
                counter -= 1

            # Decrement the frequency of the current character in the hash_map
            # This helps track how many more instances of this character are needed
            hash_map[s[end]] -= 1

            # Move the end pointer to the right to expand the window
            end += 1

            # When counter == 0, the current window contains all characters of t
            # Slide the begin pointer to shrink the window and find the smallest valid window
            while counter == 0:
                # Update the smallest window length and its starting index if the current window is smaller
                if (end - begin) < d:
                    d = end - begin
                    head = begin

                # If the character at begin is in t and its frequency is 0, increment counter
                # This indicates that the window will no longer be valid if we move begin further
                if hash_map[s[begin]] == 0:
                    counter += 1

                # Increment the frequency of the character at begin in the hash_map
                # This reflects that the character is no longer part of the current window
                hash_map[s[begin]] += 1

                # Move the begin pointer to the right to shrink the window
                begin += 1

        # If no valid window was found (d is still infinity), return an empty string
        # Otherwise, return the smallest valid window substring
        # Time Complexity: O(d) for slicing the substring, where d is the length of the smallest window
        return "" if d == float('inf') else s[head:head + d]
