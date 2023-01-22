class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= 0:
                low = mid + 1
            else:
                high = mid - 1

        pos = len(nums) - low

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= 0:
                high = mid - 1
            else:
                low = mid + 1
        return max(high+1, pos)
