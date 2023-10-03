class Solution:
    def numIdenticalPairs(self, l: List[int]) -> int:
        c = collections.Counter(l)
        s = 0
        for i in c:
            s += c[i] * (c[i]-1) // 2
        return s