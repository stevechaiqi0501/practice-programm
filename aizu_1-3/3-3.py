
while True:
    a,b=list(map(int,input().split()))
    if a and b == 0:
        break
    n=[a,b]
    n.sort()
    print(n[0],n[1])
###########################################################
while True:
    a,b=list(map(int,input().split()))
    if a and b == 0:
        break
    if a>b:
        print(a,b)
    else:
        print(b,a)
############################################################
while True:
    a,b=map(int,input().split())
    if a == 0 and b == 0:
        break
    if a<b:
        print(a,b)
    else:
        print(b,a)
    