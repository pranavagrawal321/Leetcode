class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a, b = 0, 0
        for i in s:
            a += ord(i)
        for i in t:
            b += ord(i)
        return chr(b-a)