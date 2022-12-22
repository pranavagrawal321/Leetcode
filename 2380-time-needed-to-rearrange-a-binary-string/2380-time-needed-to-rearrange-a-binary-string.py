class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        c = 0
        while "01" in s:
            c += 1
            s = s.replace("01", "10")
        return c
