import sys

sys.stdin = open("cbarn.in", "r")
sys.stdout = open("cbarn.out", "w")

l = []
ans = []
n = int(input())
for i in range(n):
    t = int(input())
    l.append(t)

for i in range(n):
    foo = 0
    for j in range(n):
        bar = (i+j)%n
        foo += l[j]*bar
    ans.append(foo)

print(min(ans))

sys.stdout.close()
