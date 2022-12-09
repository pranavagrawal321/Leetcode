class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = [i**2 for i in nums]
        i, j = 0, len(l)-1
        ans = []
        while i <= j:
            if l[i] > l[j]:
                ans.append(l[i])
                i += 1
            else:
                ans.append(l[j])
                j -= 1
        return ans[::-1]
