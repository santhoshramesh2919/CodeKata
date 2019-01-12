#distinct pairs
n=int(input())
count=0
for i in range(1,n):
    for j in range(i,n+1):
        if i!=j:
            count=count+1
print(count)
