n=input()
s=[]
vowels="aeiouAEIOU"
for i in n:
    if i in vowels and i not in s:
        print(i,end=" ")
        s.append(i)