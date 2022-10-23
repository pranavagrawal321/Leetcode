class Solution:
    def findErrorNums(self, l: List[int]) -> List[int]:
        c = Counter(l)
        # print(c)
        ans = []
        for i in range(1, len(l)+1):
            if c[i] == 2:
                ans.append(i)
                break

        for i in range(1, len(l)+1):
            if i not in c:
                ans.append(i)
                break

        return ans