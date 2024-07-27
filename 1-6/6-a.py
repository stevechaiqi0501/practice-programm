n=int(input())
a=list(map(int,input().split()))
a.reverse()
print(a)
for i in range(0,n):
    print(a[i],end='')
    if i<n-1:
        print(' ',end='')
print()#なんでこれいるの

n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True) #a.sort(reverse=True)じゃあかんのけ
print(a)
for i in range(0,n):
    print(a[i],end='')
    if i<n-1:
        print(' ',end='')
print()

#sortしてから逆数にするのか、ただ逆にするのか
