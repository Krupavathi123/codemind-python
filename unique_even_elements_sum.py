n=int(input())
L=map(int,input().split())
x=set(L)
es=0
for i in x:
   if i%2==0:
       es=es+i
print(es)