s=input()
x=s.lower()
y='aeiou'
z=0
l=[]
for ch in x:
    if ch in y and ch in x:
        l.append(ch)
for ch in y:
    if ch not in l:
        z=1
        print(ch,end=" ")
if z==0:
    print("0")