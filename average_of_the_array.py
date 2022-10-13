n=int(input())
L=list(map(int,input().split()))
s=0
for i in L:
    s=s+i
    avg=s/n
print("%.2f"%avg)