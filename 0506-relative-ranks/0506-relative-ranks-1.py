class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = dict()
        a = score.copy()
        score.sort(reverse=True)
        for i in range(len(score)):
            if i == 0:
                d[score[i]] = "Gold Medal"
            elif i == 1:
                d[score[i]] = "Silver Medal"
            elif i == 2:
                d[score[i]] = "Bronze Medal"
            else:
                d[score[i]] = str(i+1)
        for i in range(len(a)):
            a[i] = d[a[i]]
        return a