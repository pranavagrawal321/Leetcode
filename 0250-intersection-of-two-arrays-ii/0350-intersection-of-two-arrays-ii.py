class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        a = Counter(nums1)
        b = Counter(nums2)
        for i in a:
            if i in b and a[i] <= b[i]:
                l.extend([i] * a[i])
            elif i in b and a[i] > b[i]:
                l.extend([i] * b[i])

        return l
