t=input()
x=t.split()
for words in x:
    a=min(words)
    b=max(words)
    diff=abs(ord(a)-ord(b))
    print(diff,end=" ")