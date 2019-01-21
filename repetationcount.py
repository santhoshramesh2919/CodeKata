n,k=input().split(" ")
li=list(input().split(" "))
count=0
for i in range(len(li)):
    if li[i]==k:
        count+=1
print(count)
