class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        add = 0

        for i in gain:
            add += i
            ans = max(ans, add)

        return ans