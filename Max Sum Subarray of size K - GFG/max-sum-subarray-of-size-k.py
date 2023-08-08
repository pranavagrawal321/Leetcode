#User function Template for python3
class Solution:
    def maximumSumSubarray (self,k,nums,N):
        # code here 
        max_sum = sum(nums[:k])
        curr_sum = max_sum
        
        for i in range(k, len(nums)):
            curr_sum = curr_sum + nums[i] - nums[i - k]
            max_sum = max(curr_sum, max_sum)
        
        return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends