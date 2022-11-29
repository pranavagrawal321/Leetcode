class Solution:
    def oddString(self, l: List[str]) -> str:
        ans = []
        for i in l:
            t = []
            for j in range(len(i) - 1):
                t.append(ord(i[j]) - ord(i[j + 1]))
            ans.append(t)
        
        for i in range(len(ans)):
            if ans.count(ans[i]) == 1:
                return l[i]
