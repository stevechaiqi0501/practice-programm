n=int(input())
a=list(map(int,input().split()))
a.reverse()
for i in range(0,n):
    print(a[i],end='')
    if i<n-1:
        print(' ',end='')
print()#なんでこれいるの

n=int(input())
a=list(map(int,input().split()))
a.reverse() #a.sort(reverse=True)じゃあかんのけ
for i in range(0,n):
    print(a[i],end='')
    if i<n-1:
        print(' ',end='')
print()

