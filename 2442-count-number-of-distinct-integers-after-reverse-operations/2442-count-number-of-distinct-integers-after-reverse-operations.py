class Solution:
    def countDistinctIntegers(self, l: List[int]) -> int:
        c = set(l)
        for i in l:
            c.add(int(str(i)[::-1]))
        return len(c)
