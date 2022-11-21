class Solution:
    def averageValue(self, l: List[int]) -> int:
        s = 0
        c = 0
        for i in l:
            if i % 2 == 0 and i % 3 == 0:
                c += 1
                s += i
        return 0 if c == 0 else math.floor(s/c)
