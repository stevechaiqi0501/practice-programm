while True:
    
    cal = input().split()
    a=int(cal[0])
    op = cal[1]
    b=int(cal[2]) 
    
    
    if op == "?":
        break

    if op == "+":
        print(a+b)
    elif op == '-':
        print(a-b)
    elif op == '*':
        print(a*b)
    elif op == '/':
        print (int(a/b))
        
while True:
    N=list(input().split())
    
    a=int(N[0])
    op=N[1]
    b=int(N[2])
    
    if op == '?':
        break
    
    if op == '+':
        print(a+b)
    
    elif op == '-':
        print(a-b)
    
    elif op == '*':
        print(a*b)
        
    elif op == '/':
        print(a//b)
        