# https://codeforces.com/problemset/problem/231/A

n = int(input())
s = 0
for _ in range(n):
    l = list(map(int, input().split()))
    s += l.count(1)>1
print(s)