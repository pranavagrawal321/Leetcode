class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True

        for i in range(len(nums) - 1):
            inc = inc and nums[i] <= nums[i + 1]
            dec = dec and nums[i] >= nums[i + 1]

        return inc or dec