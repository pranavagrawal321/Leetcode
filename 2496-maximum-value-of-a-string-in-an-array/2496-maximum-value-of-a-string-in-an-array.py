class Solution:
    def maximumValue(self, l: List[str]) -> int:
        m = 0
        for i in l:
            if i.isnumeric():
                m = max(m, int(i))
            else:
                m = max(m, len(i))
        return m
