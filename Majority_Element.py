n=int(input())
L=list(map(int,input().split()))
mc=0
for i in range(len(L)):
  if L.count(L[i])>mc:
     mc=L.count(L[i])
     t=L[i]
print(t)