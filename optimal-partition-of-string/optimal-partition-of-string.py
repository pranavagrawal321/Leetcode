class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        d = {}

        for i in s:
            if i not in d:
                d[i] = None
            else:
                ans += 1
                d = {i: None}

        return ans + 1