a,b,c=list(map(int,input().split()))
cnt=a
score=0
while cnt <= b:
    if c % cnt == 0: #type(c/a)==int
        score += 1
    cnt += 1 #ここにcntを入れてはいけない理由は？
    
print(score)
        
##################################################
# a,b,c=map(int,input().split())
# ans=0
# for i in range (a,b+1):
#     if c%i==0:
#         ans+=1
# print(ans)
##################################################
a, b, c = list(map(int, input().split()))
ans = 0
while a <= b:
    if c % a == 0:
        ans += 1
    a += 1
print(ans)
