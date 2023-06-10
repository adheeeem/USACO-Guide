# https://codeforces.com/problemset/problem/546/A

k, n, w = map(int, input().split())

total = int(k*w*(w+1)/2)
if total > n:
    print(total-n)
else:
    print(0)