class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp_sum = sum(nums[:k])
        final_sum = temp_sum
        pointer = 0
        i = k

        while i < len(nums):
            temp_sum += nums[i] - nums[pointer]
            final_sum = max(final_sum, temp_sum)
            pointer += 1
            i += 1

        return final_sum / k