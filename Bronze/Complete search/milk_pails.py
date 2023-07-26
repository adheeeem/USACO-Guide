import sys

sys.stdin = open("pails.in", "r")
sys.stdout = open("pails.out", "w")

x, y, m = map(int, input().split())

ans = 0

r = (m // min(x, y)) + 1

for i in range(r):
    for j in range(r):
        foo = i * x + j * y
        if foo <= m:
            ans = max(ans, foo)

print(ans)

sys.stdout.close()
