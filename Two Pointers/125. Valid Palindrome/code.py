class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join(filter(str.isalnum, s))
        return filtered.lower() == filtered[::-1].lower()
