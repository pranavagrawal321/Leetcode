class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums2).intersection(set(nums1))
        m1 = min(nums1)
        m2 = min(nums2)
        return min(common) if common else min(m1, m2)*10 + max(m1, m2)