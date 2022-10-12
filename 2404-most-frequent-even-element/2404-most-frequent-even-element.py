from collections import Counter

class Solution:
    def mostFrequentEven(self, l: List[int]) -> int:
        even = list(filter(lambda x: x % 2 == 0, l))
        if len(even) == 0:
            return -1
        c = Counter(even)
        ans = []
        m = max(c.values())
        for i in c.most_common():
            if c[i[0]] == m:
                ans.append(i[0])
        return min(ans)