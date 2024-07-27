N=int(input())
list=[]
for i in range(N):
    a,b=map(int,input().split())
    c =a-b
    list.append(c)

print(abs(max(list)))