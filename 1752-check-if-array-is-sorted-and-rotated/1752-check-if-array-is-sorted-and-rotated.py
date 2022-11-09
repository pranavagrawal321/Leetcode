class Solution:
    def check(self, l: List[int]) -> bool:
        ind = None

        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                ind = i
                break

        if ind is not None:
            for i in range(ind+1, len(l)-1):
                if l[i] > l[i+1]:
                    return False
            return l[0] >= l[-1]
        else:
            return True
