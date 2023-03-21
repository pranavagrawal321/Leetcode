class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i = len(s) - 1
        ans = []
        while i >= 0:
            ans += s[i]
            if spaces and i == spaces[-1]:
                ans += " "
                spaces.pop()
            i -= 1

        return "".join(ans[::-1])