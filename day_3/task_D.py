n, m = map(int, input().split())
a = []
for i in range(n):
    stroka = list(map(int, input().split()))
    a.append(stroka)
 
d = [[0] * m for i in range(n)]
d[0][0] = a[0][0]
 
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        mx = 0
        if i > 0:
            mx = max(mx, d[i - 1][j])
        if j > 0:
            mx = max(mx, d[i][j - 1])
        if i > 0 and j > 0:
            mx = max(mx, d[i - 1][j - 1])
        d[i][j] = a[i][j] + mx
 
print(d[n - 1][m - 1])
