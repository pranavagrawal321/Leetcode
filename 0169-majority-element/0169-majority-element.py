from collections import Counter

class Solution:
    def majorityElement(self, l: List[int]) -> int:
        c = Counter(l)
        for i in c.most_common():
            if c[i[0]] > len(l)//2:
                return i[0]