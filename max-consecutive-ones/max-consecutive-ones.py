class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        final = 0

        end = 0

        while end < len(nums):
            if nums[end] == 1:
                curr += 1
            else:
                curr = 0
            final = max(curr, final)
            end += 1
        return final