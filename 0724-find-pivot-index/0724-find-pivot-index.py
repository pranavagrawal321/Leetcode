class Solution:
    def pivotIndex(self, l: List[int]) -> int:
        left = [l[0]]
        right = [l[-1]]
        for i in range(1, len(l)):
            left.append(left[-1] + l[i])
            right += [right[-1] + l[-i-1]]
        for i in range(len(l)):
            if left[i] == right[-i-1]:
                return i
        return -1
