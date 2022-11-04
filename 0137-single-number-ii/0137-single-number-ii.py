class Solution:
    def singleNumber(self, l: List[int]) -> int:
        return (3*sum(set(l)) - sum(l))//(3*len(set(l)) - len(l))
