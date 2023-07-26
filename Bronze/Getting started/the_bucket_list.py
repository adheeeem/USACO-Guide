import sys

sys.stdin = open("blist.in", "r")
sys.stdout = open("blist.out", "w")

n = int(input())
l = []
ans = 0
mx = 0
for i in range(n):
    t = list(map(int, input().split()))
    l.append(t)

check = [True for i in range(n+1)]
check1 = [True for i in range(n+1)]
l.sort()

for i in range(1, 1001):
    for j in range(n):        
        if l[j][0]<=i<=l[j][1] and check[j]:
            ans += l[j][2]
            check[j] = False

        if i > l[j][1] and check1[j] and not check[j]:
            ans -= l[j][2]
            check1[j] = False

    mx = max(ans, mx)

print(mx)

sys.stdout.close()
