class Solution:
    def countDigits(self, n: int) -> int:
        c = collections.Counter(str(n))
        ans = 0
        for i in c:
            if n % int(i) == 0:
                ans += c[i]
        return ans
