#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        curr = 0
        final = 0
        
        arr.sort()
        dep.sort()
        
        i, j = 0, 0
        
        while i < len(arr):
            if arr[i] <= dep[j]:
                curr += 1
                i += 1
            else:
                curr -= 1
                j += 1
                
            final = max(final, curr)
        
        return final



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends