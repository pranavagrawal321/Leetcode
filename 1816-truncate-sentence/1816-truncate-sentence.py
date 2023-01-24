class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        ans = []
        for i in range(k):
            ans.append(s[i])
        return " ".join(ans)
