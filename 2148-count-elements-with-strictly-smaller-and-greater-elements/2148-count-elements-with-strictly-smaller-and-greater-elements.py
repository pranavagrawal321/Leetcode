class Solution:
    def countElements(self, nums: List[int]) -> int:
        return len(list(filter(lambda x: min(nums) < x < max(nums), nums)))