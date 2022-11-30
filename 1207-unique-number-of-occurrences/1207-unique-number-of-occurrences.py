class Solution:
    def uniqueOccurrences(self, l: List[int]) -> bool:
        c = collections.Counter(l)
        return len(c) == len(set(c.values()))
