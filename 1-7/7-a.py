'''
中間試験、期末試験のいずれかを欠席した場合成績は F。
中間試験と期末試験の合計点数が 80 以上ならば成績は A 。
中間試験と期末試験の合計点数が 65 以上 80 未満ならば成績は B。
中間試験と期末試験の合計点数が 50 以上 65 未満ならば成績は C。
中間試験と期末試験の合計点数が 30 以上 50 未満ならば成績は D。 ただし、再試験の点数が 50 以上ならば成績は C。
中間試験と期末試験の合計点数が 30 未満ならば成績は F。
'''
while True:
    a,b,n=map(int,input().split())
    if a == -1 and b == -1 and n == -1:
        break
    
    if a==-1 or b==-1:
        print('F')
    else:  
        if a+b>80:
            print('A')
            
        if 65<=a+b and a+b<80:
            print('B')
            
        if 50<=a+b and a+b<65:
            print("C")
            
        if 30<=a+b and a+b<50:
            print('D')
        elif n>=50:
            print('c')
            
        if a+b<30:
            print('F')