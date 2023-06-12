class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = [False]*len(matrix)
        column = [False]*len(matrix[0])


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = True
                    column[j] = True
                    

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] or column[j]:
                    matrix[i][j] = 0
                    
        return matrix