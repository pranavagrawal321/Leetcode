from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        c = Counter(nums)
        for i in c.most_common(k):
            ans.append(i[0])
        return ans