class Solution:
    def reverse(self, x: int) -> int:
        if x < 0: 
            sign = -1
        else: 
            sign = 1
        ans = 0
        x = abs(x)
        while x > 0:
            ans = ans*10 + (x%10)
            x = x // 10
        if sign * ans in range(-2**31, 2**31):
            return sign * ans
        return 0