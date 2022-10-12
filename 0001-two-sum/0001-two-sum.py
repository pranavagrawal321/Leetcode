class Solution:
    def twoSum(self, l: List[int], t: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(l):
            if t - l[i] in hashmap:
                return [i, hashmap[t - l[i]]]
            else:
                hashmap[l[i]] = i