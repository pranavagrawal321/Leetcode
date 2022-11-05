class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 0
        while c < len(nums)-1:
            if nums[c] == nums[c+1]:
                del nums[c]
            else:
                c += 1
        return c+1
