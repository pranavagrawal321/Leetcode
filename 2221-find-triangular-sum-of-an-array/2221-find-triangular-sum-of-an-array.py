class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        ans = []

        while len(nums) > 1:
            for i in range(len(nums) - 1):
                ans.append((nums[i] + nums[i + 1])%10)
            nums = ans
            ans = []

        return nums[0]