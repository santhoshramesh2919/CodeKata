#finding the largest combination
n=int(input())
li=list(input().split(" "))
li1=[]
for i in range(0,len(li)):
    if int(li[i])==i:
        li1.append(li[i])
if (len(li1)==0):
    print("-1")    
else:    
    li1.sort()
    print(" ".join(li1))
