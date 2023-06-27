class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        add = 0
        ans = 0

        for i in gain:
            add += i
            ans = max(ans, add)
            
        return ans