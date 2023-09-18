n = int(input())

l = []

for _ in range(n):
    t = int(input())
    l.append(t)

mx = max(l) + 1
mn = min(l)
c = [0 for _ in range(mx)]

for i in l:
    c[i] = 1

for i in range(mn, mx):
    l, r = i, i
    



