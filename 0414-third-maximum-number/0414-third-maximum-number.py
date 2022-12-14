class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = list(set(nums))
        a.sort(reverse=True)
        return a[2] if len(a) > 2 else a[0]
