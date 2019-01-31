n,k=map(int,input().split())
li=list(map(int,input().split()))
li1=[]
for i in li:
    if i%2==1:
        li1.append(i)
print(li1[k-1])
