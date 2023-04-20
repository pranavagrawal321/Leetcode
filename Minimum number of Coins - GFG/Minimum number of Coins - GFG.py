# User function Template for python3

class Solution:
    def minPartition(self, n):
        # code here
        ans = []
        currency = [2000, 500, 200, 100, 50, 20, 10, 5, 2]

        for i in currency:
            while n >= i:
                ans.append(i)
                n -= i

        while n > 0:
            ans.append(1)
            n -= 1

        return ans


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()
# } Driver Code Ends