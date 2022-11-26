n=int(input())
arr=list(map(int,input().split()))
q=[]
sum=0
for i in range(len(arr)):
    x=arr[i]
    sum=0
    while x!=0:
        r=x%10
        sum=sum*10+r
        x=x//10
    print(sum,end=" ")
        