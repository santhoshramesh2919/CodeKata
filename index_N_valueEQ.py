#finding the index and value equivalences
n=int(input())
li=list(input().split(" "))
li1=[]
for i in range(0,len(li)):
    if int(li[i])==i:
        li1.append(li[i])
li1.sort()
print(" ".join(li1))
