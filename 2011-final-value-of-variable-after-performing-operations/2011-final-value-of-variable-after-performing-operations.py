class Solution:
    def finalValueAfterOperations(self, l: List[str]) -> int:
        x = 0
        for i in l:
            if i[:2] == "++" or i[1:] == "++":
                x += 1
            else:
                x -= 1
        return x
