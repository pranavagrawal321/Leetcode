# Function should return an integer value
def convertFive(N):
    # Code here
    ans = 0
    i = 0

    while N:
        if N % 10 == 0:
            ans += 5 * 10 ** i
        else:
            ans += (N % 10) * 10 ** i
        N //= 10
        i += 1

    return ans


# {
# Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        print(convertFive(int(input().strip())))
# } Driver Code Ends