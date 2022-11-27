class Solution:
    def __init__(self):
        self.d = {}

    def fib(self, n: int) -> int:
            if n in self.d:
                return self.d[n]
            if n == 0:
                return 0
            if n == 1:
                return 1
            else:
                self.d[n] = Solution().fib(n - 1) + Solution().fib(n - 2)
                return self.d[n]
