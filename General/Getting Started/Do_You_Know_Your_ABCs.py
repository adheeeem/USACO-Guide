l = list(map(int, input().split()))

abc = sum(l)//4
flag = False
for i in range(7):
    for j in range(7):
        for k in range(7):
            if k != j and j != i and l[k]+l[j]+l[i] == abc:
                flag = True
                temp = [l[k], l[j], l[i]]
                temp.sort()
                print(*temp)
                break
        if flag: break
    if flag: break

    