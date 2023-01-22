class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = 0
        sign = 1
        for i in str(n):
            s += int(i) * sign
            sign *= -1
        return s
