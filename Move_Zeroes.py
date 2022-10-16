n=int(input())
L=list(map(int,input().split()))
c=L.count(0)
r=[]
for i in range(len(L)):
  if L[i]!=0:
     r.append(L[i])
for i in range(c):
  r.append(0)
print(*r)