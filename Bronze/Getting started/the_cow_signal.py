import sys

sys.stdin = open("cowsignal.in", "r")
sys.stdout = open("cowsignal.out", "w")

m, n, k = map(int, input().split())
l = []
for i in range(m):
    temp = input()
    l.append(temp)

for i in range(m):
    for _ in range(k):
        for j in l[i]:
            print(j*k, end="")
        print()


sys.stdout.close()