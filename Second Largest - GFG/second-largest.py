#User function Template for python3
class Solution:

	def print2largest(self,l, n):
		# code here
		if len(set(l)) == 1:
		    return -1
		l = list(set(l))
		lar = l[0]
        seclar = l[1]
        for i in l:
            if i > lar:
                seclar = lar
                lar = i
            elif lar > i > seclar:
                seclar = i
        return seclar



#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends