import sys

sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")

n, m = map(int, input().split())

nn = []
mm = []

ans = 0

for i in range(n):
    a, b = map(int, input().split())
    for j in range(a):
        nn.append(b)

for i in range(m):
    a, b = map(int, input().split())
    for j in range(a):
        mm.append(b)

for i in range(100):
    ans = max(ans, mm[i]-nn[i])


print(ans)
sys.stdout.close()
