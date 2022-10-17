#User function Template for python3

class Solution:
    def reversedBits(self, n):
        # code here 
        return int(('{:032b}'.format(n))[::-1], 2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends