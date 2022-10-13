class Solution:
    def isSameAfterReversals(self, n: int) -> bool:
        temp = n
        ans = 0
        while n > 0:
            ans = ans*10 + (n%10)
            n = n // 10
        nans = 0
        while ans > 0:
            nans = nans*10 + (ans%10)
            ans = ans // 10
        return temp == nans