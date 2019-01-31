#values in odd positions
n=input()
li=[]
for i in n:
    if int(i)%2==1:
        li.append(i)
print(*li)
