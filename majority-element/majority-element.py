class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = nums[0]
        vote = 1

        for i in range(1, len(nums)):
            if vote == 0:
                ele = nums[i]
            if nums[i] == ele:
                vote += 1
            else:
                vote -= 1

        return ele