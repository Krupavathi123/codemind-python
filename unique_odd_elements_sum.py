n=int(input())
L=map(int,input().split())
x=set(L)
os=0
for i in x:
   if i%2!=0:
       os=os+i
print(os)