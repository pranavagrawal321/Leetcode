class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0

        left = [height[0]]
        right = [height[-1]]

        for i in range(1, len(height)):
            left.append(max(left[-1], height[i]))
            
        for i in range(len(height)-2, -1, -1):
            right.append(max(right[-1], height[i]))

        right = right[::-1]

        for i in range(len(height)):
            ans += min(left[i], right[i]) - height[i]

        return ans