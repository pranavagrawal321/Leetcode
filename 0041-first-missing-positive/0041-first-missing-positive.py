class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if max(nums) < 1:
            return 1
        a = set(nums)
        for i in range(1, max(a)+2):
            if i not in a:
                return i