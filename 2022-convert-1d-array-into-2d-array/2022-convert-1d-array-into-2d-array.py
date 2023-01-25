from numpy import array

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n == len(original):
            a = array(original)
            return a.reshape(m, n)
        else:
            return []