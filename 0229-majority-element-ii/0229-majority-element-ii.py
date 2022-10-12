from collections import Counter

class Solution:
    def majorityElement(self, l: List[int]) -> List[int]:
        c = Counter(l)
        ans = []
        for i in c.most_common():
            if c[i[0]] > len(l)//3:
                ans.append(i[0])
        return ans