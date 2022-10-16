n=int(input())
L=list(map(int,input().split()))
s=0
for i in range(len(L)-1,0,-1):
  if L[i]-L[i-1]>0:
     s+=L[i]-L[i-1]
print(s)