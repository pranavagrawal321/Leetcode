class Solution:
    def prefixesDivBy5(self, l: List[int]) -> List[bool]:
        s = ""
        ans = []
        for i in l:
            s += str(i)
            ans.append(int(s, 2)%5==0)
        return ans
