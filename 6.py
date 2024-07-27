L = []
cnt = 0
N,K = map(int,input().split())
for i in range(N):
    n=int(input())
    L.append(n)
    
for j in range(len(L)):
    for k in range(len(L)):
        if L[k] + L[j] == K:
            cnt += 1
            
print(cnt)