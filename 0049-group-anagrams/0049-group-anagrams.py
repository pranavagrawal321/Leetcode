class Solution:
    def groupAnagrams(self, l: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in l:
            d[tuple(sorted(i))].append(i)
        return d.values()