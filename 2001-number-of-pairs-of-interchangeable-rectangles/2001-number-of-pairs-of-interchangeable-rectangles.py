class Solution:
    def interchangeableRectangles(self, l: List[List[int]]) -> int:
        d = {}
        s = 0
        for i in l:
            if i[0]/i[1] not in d:
                d[i[0]/i[1]] = 1
            else:
                d[i[0]/i[1]] += 1
        for i in d:
            s += d[i] * (d[i] - 1) // 2
        return s
