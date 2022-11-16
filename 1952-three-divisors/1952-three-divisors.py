class Solution:
    def isThree(self, n: int) -> bool:
        s = set()
        for i in range(2, int(n**0.5) + 1):
            if n%i == 0:
                s.add(i)
                s.add(n//i)
        return len(s) == 1
