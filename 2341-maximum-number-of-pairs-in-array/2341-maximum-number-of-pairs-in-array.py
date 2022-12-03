class Solution:
    def numberOfPairs(self, l: List[int]) -> List[int]:
        c = Counter(l)
        i = 0
        for i in c:
            while c[i] >= 2:
                c[i] -= 2
        return (len(l) - sum(c.values()))//2, sum(c.values())
