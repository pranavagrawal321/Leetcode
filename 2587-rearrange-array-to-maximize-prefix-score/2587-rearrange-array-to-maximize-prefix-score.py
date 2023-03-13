class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        c = 0

        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]

        for i in range(len(nums)):
            if nums[i] > 0:
                c += 1

        return c