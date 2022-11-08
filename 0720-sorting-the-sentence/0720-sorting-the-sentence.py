class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        ans = ""
        for i in " ".join(sorted(s, key=lambda x: x[-1])).split():
            ans += i[:-1]+" "
        return ans[:-1]
