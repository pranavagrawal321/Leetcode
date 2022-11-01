class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i, j in enumerate(nums):
            if j in hashmap and i - hashmap[j] <= k:
                return True
            else:
                hashmap[j] = i
        return False