class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l = [[], []]
        for i in nums1:
            if i not in nums2 and i not in l[0]:
                l[0].append(i)
        for i in nums2:
            if i not in nums1 and i not in l[1]:
                l[1].append(i)
        return l
