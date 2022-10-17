#User function Template for python3

class Solution:    
    #Complete this function
    def printNos(self,n, i=1):
        #Your code here
       if i == n+1:
           return 
       print(i, end=" ")
       return Solution().printNos(n, i+1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        ob=Solution()
        
        ob.printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends