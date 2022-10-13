n=int(input())
l=list(map(int,input().split()))
avg=sum(l)//n
if avg in l:
    print("True")
else:
    print("False")