class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for i in range(2, math.isqrt(n)+1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
        return is_prime.count(True)
