import sys

sys.stdin = open("cowqueue.in", "r")
sys.stdout = open("cowqueue.out", "w")

n = int(input())

l = []
ans = 0
curr = 0
for i in range(n):
    t = list(map(int, input().split()))
    l.append(t)

l.sort()

ans = sum(l[0])

for i in range(1, n):
    a, b = l[i]
    if ans > a:
        ans += b
    else:
        ans = a+b

print(ans)

sys.stdout.close()
        


