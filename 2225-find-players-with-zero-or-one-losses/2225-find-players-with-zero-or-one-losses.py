class Solution:
    def findWinners(self, l: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)

        for i in l:
            d[i[1]] += 1

        a = []
        b = []

        for i in l:
            if d[i[0]] == 0:
                a.append(i[0])

        for i in d:
            if d[i] == 1:
                b.append(i)

        return sorted(set(a)), sorted(b)
