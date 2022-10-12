from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        c = Counter(s)
        for i in c.most_common():
            ans += i[0]*i[1]
        return ans