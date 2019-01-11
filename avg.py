n=int(input())
total=0
li=list(input().split(" "))
for i in range(len(li)):
    total+=int(li[i])
print(total//len(li))
    
