s=input()
w=s.split()
for i in range(len(w)):
    if i%2==0:
        print(w[i][::-1],end=" ")
    else:
        print(w[i],end=" ")