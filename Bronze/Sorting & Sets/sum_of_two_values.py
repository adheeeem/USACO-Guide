n, x = map(int, input().split())
l = list(map(int, input().split()))
temp = [0 for i in range(max(l)+1)]

flag = True

for i in l:
    temp[i] = 1


for i in range(n):
    if x-l[i] > 0 and x-l[i] < len(temp) and temp[x-l[i]] == 1:
        ind1 = i+1
        ind2 = l.index(x-l[i])+1
        if ind1 != ind2:
            print(ind1, ind2)
            flag = False
            break

if flag: print("IMPOSSIBLE")

