class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(n):
            if n == 1:
                return False
            for i in range(2, isqrt(n)+1):
                if n % i == 0:
                    return False
            return True


        ans = 0
        for i in range(len(nums)):
            if is_prime(nums[i][i]):
                ans = max(ans, nums[i][i])
            if is_prime(nums[i][len(nums) - i - 1]):
                ans = max(ans, nums[i][len(nums) - i - 1])
        return ans