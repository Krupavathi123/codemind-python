s=input()
vowels="aeiou"
v=[i for i in vowels if i not in s]    
if len(v)==0:
    print(0)
else:
    print(*v)
    