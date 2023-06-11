class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        nums.remove(max(nums))
        nums.remove(min(nums))
        return nums[0]