class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        max_so_far = 0
        max_final = -float("inf")

        for i in arr:
            max_so_far += i
            if max_so_far > max_final:
                max_final = max_so_far
            if max_so_far < 0:
                max_so_far = 0
        return max_final