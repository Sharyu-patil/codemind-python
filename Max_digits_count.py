n=int(input())
a=list(map(str,input().split()))
x=[]
y=[]
for i in a:
    x.append(len(i))
for i in range(n):
    if(x[i]==max(x)):
        y.append(x[i])
print(len(y))