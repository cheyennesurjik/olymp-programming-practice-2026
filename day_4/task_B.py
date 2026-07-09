t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    res = 2 * n - k - 2 * max(a) + 1
    print(res)
