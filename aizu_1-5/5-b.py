while True:
    H,W=map(int,input().split())
    
    if H==0 and W==0:
        break
    
    if H >=3 and W>=3:
        print("#"*W)
        for i in range(H-2):
            print('#','.'*(W-2),'#',sep='')
        print("#"*W)
            
    print()