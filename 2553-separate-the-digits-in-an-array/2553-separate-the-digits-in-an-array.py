class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums[::-1]:
            num = i
            while num > 0:
                ans.append(num % 10)
                num = num // 10
        return ans[::-1]