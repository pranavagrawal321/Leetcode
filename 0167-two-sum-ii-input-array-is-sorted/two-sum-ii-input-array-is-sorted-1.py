class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, j in enumerate(numbers):
            if target - j in seen:
                return seen[target-j]+1, i+1
            seen[j] = i
