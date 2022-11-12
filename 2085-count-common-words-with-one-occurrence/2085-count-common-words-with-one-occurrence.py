class Solution:
    def countWords(self, l1: List[str], l2: List[str]) -> int:
        c1 = Counter(l1)
        c2 = Counter(l2)
        c = 0
        for i in c1:
            if c1[i] == 1 and c2[i] == 1:
                c += 1
        return c
