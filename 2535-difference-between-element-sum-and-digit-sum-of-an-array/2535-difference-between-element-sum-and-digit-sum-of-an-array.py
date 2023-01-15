class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            while i > 0:
                s += i % 10
                i = i // 10
        return abs(s - sum(nums))
