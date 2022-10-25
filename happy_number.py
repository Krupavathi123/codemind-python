def fun(n):
    s=0
    while n!=0:
        r=n%10
        s=s+(r**2)
        n=n//10
    return s
n=int(input())
while n>9:
    n=fun(n)
if n==1 or n==7:
    print(True)
else:
    print(False)