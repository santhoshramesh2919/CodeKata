li=list(input())
li1=[]
for i in li:
    if i in li1:
        print("No")
        break
    else:
        li1.append(i)
else:
    print("Yes")
