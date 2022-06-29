n=input()
x=n.split()
count=0
max=0
for word in x:
    count=0
    for charecter in word:
        count=count+1
    print(count,end=" ")    