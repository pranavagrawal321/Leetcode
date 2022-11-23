class Solution:
    def mergeSimilarItems(self, l1: List[List[int]], l2: List[List[int]]) -> List[List[int]]:
        d = {}
        for i in l1:
            if i[0] not in d:
                d[i[0]] = i[1]
            else:
                d[i[0]] += i[1]

        for i in l2:
            if i[0] not in d:
                d[i[0]] = i[1]
            else:
                d[i[0]] += i[1]

        return [[k,v] for k,v in sorted(d.items())]
