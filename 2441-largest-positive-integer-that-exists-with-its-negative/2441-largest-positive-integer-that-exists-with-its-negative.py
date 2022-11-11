class Solution:
    def findMaxK(self, l: List[int]) -> int:
        ans = -float('inf')
        h = set()
        for i in l:
            if -i not in h:
                h.add(i)
            else:
                ans = max(abs(i), ans)
        return ans if ans > -float("inf") else -1
