# Function should return an integer value
def convertFive(N):
    # Code here
    ans = 0

    while N:
        if N % 10 == 0:
            ans = ans * 10 + 5
        else:
            ans = ans * 10 + N % 10
        N //= 10

    return int(str(ans)[::-1])


# {
# Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        print(convertFive(int(input().strip())))
# } Driver Code Ends