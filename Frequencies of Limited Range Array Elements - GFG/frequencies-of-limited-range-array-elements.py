class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        hashmap = {}
       
        for i in arr:
            hashmap[i] = 1+hashmap.get(i,0)

        # get function is used to avoid key error
        for i in range(N):
            arr[i] = hashmap[i+1] if i+1 in hashmap else 0



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		arr=[int(x) for x in input().strip().split()]
		P=int(input())
		ob=Solution()
		ob.frequencyCount(arr, N, P)
		for i in arr:
			print(i, end=" ")
		print()
		T-=1



# } Driver Code Ends