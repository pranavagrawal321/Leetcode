# User function Template for python3
from math import log10


class Solution:
    def isPowerof3(ob, N):
        # code here
        if N <= 0:
            return "No"
        return "Yes" if (log10(N) / log10(3)).is_integer() else "No"


# {
# Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.isPowerof3(N))
# } Driver Code Ends