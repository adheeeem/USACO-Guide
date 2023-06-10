import sys

#sys.stdin = open("word.in", "r")
#sys.stdout = open("word.out", "w")

n, k = map(int, input().split())
l = input().split()
s = 0
ans = ""
foo = []
for i in range(len(l)):
    if len(ans+l[i]) <= k:
        ans += l[i] + " "
    else:
        foo.append(ans)
        ans = l[i]
print(foo)

#sys.stdout.close()