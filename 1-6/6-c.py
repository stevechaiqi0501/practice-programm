n = int(input())
inf = [[[[0]*10]*3] for i in range(4)]
for i in range(n):
    b,f,r,v=map(int,input().split())
    inf[b][f][r] += v
print(inf)