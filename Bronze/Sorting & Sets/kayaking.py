n = int(input())
l = list(map(int, input().split()))
n *= 2
l.sort()
full = l[:]
mn = sum(l)

def calc_diff(ls):
    ans = 0
    for i in range(0, n-2, 2):
        ans += ls[i+1]-ls[i]
    return ans

for i in range(n):
    for j in range(i+1, n):
        t1 = l[i]
        t2 = l[j]
        l.remove(t1)
        l.remove(t2)
        mn = min(mn, calc_diff(l))
        l = full[:]

print(mn)
    
