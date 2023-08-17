d = {}

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in d:
            d[n] = Solution().climbStairs(n-1) + Solution().climbStairs(n-2) 
        return d[n]