class Solution:
    def distinctAverages(self, l: List[int]) -> int:
        l.sort()
        i, j = 0, len(l)-1
        ans = set()
        while i < j:
            ans.add((l[i] + l[j])/2)
            i += 1
            j -= 1
        return len(ans)
