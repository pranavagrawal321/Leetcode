class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        c = 0

        while k > 0 and (numNegOnes or numZeros or numOnes):
            if numOnes:
                c += 1
                numOnes -= 1
                k -= 1
            elif numZeros:
                k -= 1
                numZeros -= 1
            elif numNegOnes:
                numNegOnes -= 1
                c -= 1
                k -= 1


        return c