class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = score.copy()
        d = dict()
        temp.sort(reverse=True)
        for i in temp:
            d[i] = temp.index(i) + 1
        ans = [str(d[i]) for i in score]
        ans[ans.index("1")] = "Gold Medal"
        if "2" in ans:
            ans[ans.index("2")] = "Silver Medal"
        if "3" in ans:
            ans[ans.index("3")] = "Bronze Medal"
        return ans
