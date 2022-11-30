class Solution:
    def kthSmallest(self, l: List[List[int]], k: int) -> int:
        return sorted([i for j in l for i in j])[k-1]
