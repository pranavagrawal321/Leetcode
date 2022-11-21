class Solution:
    def distinctAverages(self, l: List[int]) -> int:
        s = set()
        i = 0
        while i < len(l):
            a, b = min(l), max(l)
            s.add((a+b)/2)
            l.remove(a)
            l.remove(b)
        return len(s)
