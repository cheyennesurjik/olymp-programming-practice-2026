t = int(input())
for q in range(t):
    n, c, d = map(int, input().split())
    b = list(map(int, input().split()))
    b.sort()
    first = b[0]
    a = []
    for i in range(n):
        for j in range(n):
            a.append(first + i * c + j * d)
    a.sort()
    if b == a:
        print("YES")
    else:
        print("NO")
