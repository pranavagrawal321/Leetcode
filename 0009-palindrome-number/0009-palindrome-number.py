class Solution:
    def isPalindrome(self, n: int) -> bool:
        ans = 0
        temp = n
        while n > 0:
            ans = ans*10 + (n%10)
            n = n // 10
        return ans == temp