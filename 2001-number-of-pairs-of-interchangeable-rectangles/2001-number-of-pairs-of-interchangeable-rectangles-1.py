class Solution:
    def interchangeableRectangles(self, l: List[List[int]]) -> int:
        d = defaultdict(int)
        s = 0
        for i in l:
            d[i[0]/i[1]] += 1
        for i in d:
            s += d[i] * (d[i] - 1) // 2
        return s
