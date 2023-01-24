class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s = 0
        c = collections.Counter(nums)
        for i in c:
            if c[i] == 1:
                s += i

        return s
