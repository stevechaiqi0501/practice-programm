def isOdd(n):
    if n%2 == 0:
        result = 0
    else:
        result = 1
        
    return result

n = int(input())

x = isOdd(n)  # 提出された関数を実行

print(x)