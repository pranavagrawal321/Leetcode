class Solution:
    def search(self, arr: List[int], target: int) -> int:
        low = 0
        high = len(arr) - 1
        for i in range(len(arr)):
            mid = (low + high)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1