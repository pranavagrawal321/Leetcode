class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        a = []
        for i in mat:
            a.extend(i)

        if r*c != len(a):
            return mat
        else:
            ans = []
            for i in range(0, r*c, c):
                ans.append(a[i: i+c])
            return ans