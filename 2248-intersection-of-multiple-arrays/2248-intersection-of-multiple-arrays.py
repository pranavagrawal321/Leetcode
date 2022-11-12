class Solution:
    def intersection(self, l: List[List[int]]) -> List[int]:
        ans = l[0]
        for i in range(len(l)):
            ans = set(ans).intersection(set(l[i]))
        return sorted(ans)
