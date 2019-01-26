#finding the largest combination
n=int(input())
li=list(input().split(" "))
li1=[]
while (len(li)!=0):
    li1.append(max(li))
    li.pop(li.index(max(li)))
print("".join(li1))
