class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            divisible = True
            if "0" in str(i):
                continue
            for j in str(i):
                if i%int(j) != 0:
                    divisible = False
            if divisible:
                ans.append(i)
        return ans