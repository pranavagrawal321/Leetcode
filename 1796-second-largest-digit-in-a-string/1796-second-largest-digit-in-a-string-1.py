class Solution:
    def secondHighest(self, s: str) -> int:
        l = set()
        for i in s:
            if i.isnumeric():
                l.add(i)
        return -1 if len(l) <= 1 else sorted(l)[-2]
