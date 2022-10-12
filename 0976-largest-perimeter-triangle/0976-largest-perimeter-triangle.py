class Solution:
    def largestPerimeter(self, l: List[int]) -> int:
        l.sort(reverse=True)
        for i in range(len(l)-2):
            if l[i] < l[i+1] + l[i+2]:
                return l[i]+l[i+1]+l[i+2]
        else:
            return 0