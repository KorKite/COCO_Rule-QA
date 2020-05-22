n = int(input())
dp = [[None for i in range(n)] for i in range(n)]
for i in range(n):
    a = list(map(int, input().split(" ")))
    if i != 0:
        for j in range(i+1):
            dp[i][j] = list(a)[j]
    else:
        dp[i][0] = list(a)[0]



for i in range(1,n):
    for j in range(i+1):

        if j == 0:

            dp[i][j] = dp[i][j] + dp[i-1][j]

        elif j == i:
            dp[i][j] = dp[i][j] + dp[i-1][j-1]

        else:

            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + dp[i][j]


print(max(dp[-1]))
