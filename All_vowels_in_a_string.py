s=input()
vowels="aeiouAEIOU"
uc=[i for i in vowels if i in s and i.isupper()]  
Lc=[i for i in vowels if i in s and i.islower()]
x=set(uc)
y=set(Lc)
if len(x)==5 or len(y)==5:
    print("True")
else:
    print("False")
    