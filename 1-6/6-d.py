n,m=map(int,input().split())
a=[list(map(int,input().split())) for i in range(n)]
b=[0]*m

for i in range(m):
    b[i] = int(input())
    
c=[0]*n
for i in range(n):
    for j in range(m):
        c[i]+=a[i][j]*b[j]
for i in range(n):
    print(c[i])