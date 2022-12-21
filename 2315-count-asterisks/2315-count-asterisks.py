class Solution:
    def countAsterisks(self, s: str) -> int:
        s = s.split("|")
        ans = 0
        for i in range(len(s)):
            if i % 2 == 0:
                ans += s[i].count("*")
        return ans
