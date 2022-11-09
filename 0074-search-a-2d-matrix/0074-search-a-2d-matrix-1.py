class Solution:
    def searchMatrix(self, l: List[List[int]], t: int) -> bool:
        def binary_search(arr):
            low = 0
            high = len(arr) - 1
            while low <= high:
                mid = (low + high)//2
                if arr[mid] == t:
                    return True
                elif arr[mid] < t:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

        for i in l:
            if i[0] <= t <= i[-1]:
                return binary_search(i)
        return False
