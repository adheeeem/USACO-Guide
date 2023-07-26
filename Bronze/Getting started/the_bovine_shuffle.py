import sys

sys.stdin = open("shuffle.in", "r")
sys.stdout = open("shuffle.out", "w")

n = int(input())
l = list(map(int, input().split()))
ids = input().split()

res = [0 for _ in range(n+1)]

for i in range(n):
    res[l[i]] = ids[i]

for i in res[1:]:
    print(i)

sys.stdout.close()
