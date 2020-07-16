ip=list(map(str,input().split()))

def super_digit(n):
    sum=0
    if len(n)==1:
        print(n)
        
    else:
        a=len(n)
        for i in range(a):
            sum=sum+int(n[i])
        
        super_digit(str(sum))
               
sum=0
num=len(ip[0])
for i in range(num):
            sum=sum+int(ip[0][i])
n=sum*int(ip[1])

c=super_digit(str(n))
