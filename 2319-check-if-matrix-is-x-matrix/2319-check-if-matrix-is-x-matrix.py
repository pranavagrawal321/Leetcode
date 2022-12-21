class Solution:
    def checkXMatrix(self, l: List[List[int]]) -> bool:
        for i in range(len(l)):
            for j in range(len(l[0])):
                if i == j or i + j == len(l) - 1:
                    if l[i][j] == 0:
                        return False
                else:
                    if l[i][j] != 0:
                        return False
        return True
