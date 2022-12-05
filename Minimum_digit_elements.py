n=int(input())
a=list(map(str,input().split()))
c=0
count=0
k=0
minn=999
x=[]
for i in a:
    x.append(len(i))
a1=[]
for i in range(len(x)):
    if(x[i]==min(x)):
        a1.append(x[i])
        
print(len(a1))