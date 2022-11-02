class Solution:
    def findPeakElement(self, nums) -> int:
        low = 0
        high = len(nums)-1
        while low <= high-1:
            mid = (low + high)//2
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid - 1
        return low


# print(Solution().findPeakElement([3,1,2]))