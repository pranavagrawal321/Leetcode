class Solution:
    def greatestLetter(self, s: str) -> str:
        seen = set()
        ans = ""
        for i in s:
            seen.add(i)
            if i.upper() in seen and i.lower() in seen:
                ans = max(ans, i.upper())
        return ans
