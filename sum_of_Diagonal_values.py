n,m=map(int,input().split())
mat=[]
for i in range (n):
    L=list(map(int,input().split()))
    mat.append(L)
s=0
for i in range(n):
  for j in range(m):
    if i==j or i+j==n-1:
        s=s+mat[i][j]
print(s)
    