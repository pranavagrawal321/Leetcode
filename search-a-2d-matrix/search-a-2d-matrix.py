class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])

        start = 0
        end = row * column - 1

        while start <= end:
            mid = (start + end) // 2
            if matrix[mid//column][mid%column] == target:
                return True
            elif matrix[mid//column][mid%column] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False