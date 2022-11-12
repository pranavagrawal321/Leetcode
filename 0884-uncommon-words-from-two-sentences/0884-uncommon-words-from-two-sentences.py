class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c1 = Counter(s1.split())
        c2 = Counter(s2.split())
        ans = []
        for i in c1:
            if c1[i] == 1 and c2[i] == 0:
                ans.append(i)

        for i in c2:
            if c2[i] == 1 and c1[i] == 0:
                ans.append(i)

        return ans
