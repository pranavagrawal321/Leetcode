#User function Template for python3
class Solution:

	def findMaximum(self,nums, n):
		# code here
		low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if (mid == 0 and nums[mid] > nums[mid+1]) or (mid == n-1 and nums[mid] > nums[mid-1]) or nums[mid-1] < nums[mid] > nums[mid + 1]:
                return nums[mid]
            elif nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
        return low


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends