class Solution:
    def mergeSimilarItems(self, l1: List[List[int]], l2: List[List[int]]) -> List[List[int]]:
        a = Counter(dict(l1)) + Counter(dict(l2))
        return [list(i) for i in sorted(a.items())]
