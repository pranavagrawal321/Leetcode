class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1 = None
        ele2 = None

        c1 = 0
        c2 = 0

        for i in range(len(nums)):
            if nums[i] == ele1:
                c1 += 1
            elif nums[i] == ele2:
                c2 += 1
            elif c1 == 0:
                ele1 = nums[i]
                c1 = 1
            elif c2 == 0:
                ele2 = nums[i]
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1

        ans = []
        if nums.count(ele1) > len(nums)/3:
            ans.append(ele1)

        if nums.count(ele2) > len(nums)/3:
            ans.append(ele2)
        
        return ans