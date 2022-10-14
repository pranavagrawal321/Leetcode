class Solution:
    def sortPeople(self, n: List[str], h: List[int]) -> List[str]:
        c = {}
        for i in range(len(n)):
            c[h[i]] = n[i]
        ans = []
        for i in sorted(c.keys(), reverse=True):
            ans.append(c[i])
        return ans