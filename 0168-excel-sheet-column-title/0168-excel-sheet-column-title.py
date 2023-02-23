class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        columnNumber -= 1
        while columnNumber >= 0:
            ans += chr(ord('A') + columnNumber % 26)
            columnNumber //= 26
            columnNumber -= 1

        return ans[::-1]
