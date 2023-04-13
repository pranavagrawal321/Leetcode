class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        ans = []
        j = 0

        for i in pushed:
            ans.append(i)
            while ans and ans[-1] == popped[j]:
                ans.pop()
                j += 1
        return ans == []