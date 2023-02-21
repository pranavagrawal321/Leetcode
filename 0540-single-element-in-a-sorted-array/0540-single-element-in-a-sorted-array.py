class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    start = mid + 2
                else:
                    end = mid
            else:
                if nums[mid] == nums[mid - 1]:
                    start = mid + 1
                else:
                    end = mid - 1

        return nums[start]