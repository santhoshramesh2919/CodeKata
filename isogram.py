li=list(input())
li1=[]
for i in li:
    if i in li1:
        print("no")
        break
    else:
        li1.append(i)
else:
    print("yes")
