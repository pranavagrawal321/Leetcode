class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        def intersect(nums1, nums2):
            l = []
            a = Counter(nums1)
            b = Counter(nums2)
            for i in a:
                if i in b and a[i] <= b[i]:
                    l.extend([i] * a[i])
                elif i in b and a[i] > b[i]:
                    l.extend([i] * b[i])

            return l
    
        ans = words[0]
        for i in words:
            ans = intersect(ans, i)
        return ans
