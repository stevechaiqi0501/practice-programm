n=[1,2,3]
l=len(n)
print(l)
print('###########################################')
n = list(map(int,input().split()))
for k in range(len(n)):
    
    if n[k] == 0:
        break
    
    print('Case ',k+1,': ',n[k],sep='')
    
print('#############################################')

cnt=0
while True: 
    x=int(input()) #こうすれば縦一列にinput可能
    if x==0:
        break
    cnt+=1
    print("Case ",cnt,": ",x,sep='')

