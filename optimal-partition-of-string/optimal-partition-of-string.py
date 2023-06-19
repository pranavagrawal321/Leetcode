class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        d = set()

        for i in s:
            if i not in d:
                d.add(i)
            else:
                ans += 1
                d = set()
                d.add(i)

        return ans + 1