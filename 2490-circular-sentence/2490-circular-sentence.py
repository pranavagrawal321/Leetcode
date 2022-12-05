class Solution:
    def isCircularSentence(self, s: str) -> bool:
        l = s.split()
        for i in range(len(l)-1):
            if l[i][-1] != l[i+1][0]:
                return False
        else:
            return l[-1][-1] == l[0][0]
