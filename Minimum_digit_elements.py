n=int(input())
a=list(map(str,input().split()))
a1=[]
a2=[]
for i in a:
    a1.append(len(i))
for i in range(len(a1)):
    if(a1[i]==min(a1)):
        a2.append(a1[i])
print(len(a2))