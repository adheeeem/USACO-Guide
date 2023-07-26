import sys

sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")

abc = [0 for i in range(26)]
n = int(input())

l = []
for i in range(n):
    l.append(input().split())

for i in range(97, 123):
    for j in l:
        mx = max(j[0].count(chr(i)), j[1].count(chr(i)))
        abc[i-97] += mx

for i in abc:
    print(i)
        

sys.stdout.close()
