def count_vowels(word):
    vowels="aeiou"
    cnt=0
    for i in word:
        if i in vowels:
            cnt=cnt+1
    return cnt
s=input()
words=s.split()
view=[count_vowels(i) for i in words]
print(*view)