class Solution:
    def runningSum(self, l: List[int]) -> List[int]:
        for i in range(1, len(l)):
            l[i] += l[i-1]
        return l
