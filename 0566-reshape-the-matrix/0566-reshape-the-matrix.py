from numpy import array

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        arr = array(mat)
        try:
            return arr.reshape(r, c)
        except ValueError:
            return mat