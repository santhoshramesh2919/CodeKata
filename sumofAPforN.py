a,d,n=map(int,input().split())
li=[]
for i in range(n):
    if i==0:
        li.append(a)
    else:
        li.append(li[i-1]+d)
print(sum(li))
