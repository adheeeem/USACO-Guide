import sys

sys.stdin = open("diamond.in", "r")
sys.stdout = open("diamond.out", "w")

n, k = map(int, input().split())
sz = []

for i in range(n):
    s = int(input())
    sz.append(s)

sz.sort()
ans = 0

for i in range(n):
    tm = 0
    for j in range(i, n):
        if sz[j]-sz[i] <= k: tm += 1
        else:
            ans = max(ans, tm)
            break
        
print(ans)

sys.stdout.close()
