class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1] * len(nums)

        add = sum(nums[:2 * k])
        for i in range(k, len(nums) - k):
            add += nums[i + k]
            ans[i] = add // (2 * k + 1)
            add -= nums[i - k]


        return ans