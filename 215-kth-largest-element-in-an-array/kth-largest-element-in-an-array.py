from sortedcontainers import SortedList

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return SortedList(nums)[-k]