while True:
    W,H=map(int,input().split())
    if H==0 and W==0:
        break
    
    for i in range(0,H):
        for j in range(0,W):
            if (i+j)%2==0:
                print('.' ,end='')
            else:
                print('#', end='')
        print()#なんでこれで改行になるの
                
    print()