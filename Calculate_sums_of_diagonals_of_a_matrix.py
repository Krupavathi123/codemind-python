num=int(input())
l=[]
for i in range(num):
    t=list(map(int,input().split()))
    l.append(t)
fd=0
sd=0
l1=[]
for i in range(len(l)):
    l1.append(l[i][::-1])
for i in range(len(l)):
    for j in range(len(l)):
        if i==j:
            fd+=l[i][j]
            sd+=l1[i][j]
print("Principal Diagonal:",end="")
print(fd)
print("Secondary Diagonal:",end="")
print(sd)
            