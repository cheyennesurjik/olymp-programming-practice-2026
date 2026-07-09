T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    c = []
    for i in range(n):
        r = [0] + list(map(int, input().split()))
        c.append(r)
    dp = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(n):
        for s in range(m + 1):
            dp[i + 1][s] = dp[i][s]
            for j in range(1, s + 1):
                if dp[i][s - j] + c[i][j] > dp[i + 1][s]:
                    dp[i + 1][s] = dp[i][s - j] + c[i][j]
    print(dp[n][m])
