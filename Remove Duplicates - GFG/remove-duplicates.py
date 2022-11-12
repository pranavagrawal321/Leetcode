#User function Template for python3
class Solution:
	def removeDups(self, S):
		# code here
		n = ""
		for i in S:
		    if i not in n:
		        n += i
        return n


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeDups(s)
		
		print(answer)


# } Driver Code Ends