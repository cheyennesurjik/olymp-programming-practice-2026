n, k = map(int, input().split())
a = list(map(int, input().split()))
n1 = n // 2
n2 = n - n1
left = [[] for i in range(n1 + 1)]
right = [[] for i in range(n2 + 1)]

for mask in range(1 << n1):
    xor_val = 0
    size = 0
    for i in range(n1):
        if mask & (1 << i):
            xor_val ^= a[i]
            size += 1
    left[size].append(xor_val)

for mask in range(1 << n2):
    xor_val = 0
    size = 0
    for i in range(n2):
        if mask & (1 << i):
            xor_val ^= a[n1 + i]
            size += 1
    right[size].append(xor_val)

for i in range(n1 + 1):
    left[i].sort()
for i in range(n2 + 1):
    right[i].sort()

res = 0

for i in range(n1 + 1):
    j = k - i
    if j < 0 or j > n2:
        continue
    for x in left[i]:
        for y in right[j]:
            now = x ^ y
            if now > res:
                res = now

print(res)
