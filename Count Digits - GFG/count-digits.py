#User function Template for python3


class Solution:
    def evenlyDivides (self, n):
        # code here
        c = 0
        for i in str(n):
            try:
                if n%int(i) == 0:
                    c += 1
            except ZeroDivisionError:
                continue
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends