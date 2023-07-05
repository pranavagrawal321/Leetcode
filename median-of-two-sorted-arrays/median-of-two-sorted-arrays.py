class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = []
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                ans.append(nums2[j])
                j += 1
            else:
                ans.append(nums1[i])
                j += 1

        while i < len(nums1):
            ans.append(nums1[i])
            i += 1

        while j < len(nums2):
            ans.append(nums2[j])
            j += 1

        return ans[len(ans) // 2] if len(ans) % 2 == 1 else (ans[len(ans) // 2] + ans[len(ans) // 2 - 1]) / 2