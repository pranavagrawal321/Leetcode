class Solution:
    def secondHighest(self, s: str) -> int:
        l = []
        for i in s:
            if i.isnumeric():
                l.append(i)
        return -1 if len(set(l)) <= 1 else sorted(set(l))[-2]
