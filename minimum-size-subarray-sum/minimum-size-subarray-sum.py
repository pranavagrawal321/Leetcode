class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        add = 0
        left = 0

        for i in range(len(nums)):
            add += nums[i]
            
            while add >= target:
                add -= nums[left]
                ans = min(ans, i - left + 1)
                left += 1

        return 0 if ans == float("inf") else ans