class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        for i in nums:
            if ans and ans[-1][1] == i - 1:
                ans[-1][1] = i
            else:
                ans.append([i, i])
                
        return [str(i[0])+"->"+str(i[1]) if i[0] != i[1] else str(i[0]) for i in ans]