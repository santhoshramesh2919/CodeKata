n,k=input().split(" ")
li=list(input().split(" "))
for i in range(len(li)):
    if li[i]==k:
        print("yes")
        break;
if i==len(li)-1:
    print("no")
