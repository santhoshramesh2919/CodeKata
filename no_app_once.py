#finding the number which appaers once
n=int(input())
li=list(input().split(" "))
dic1=(set(li))
rs={}
for i in dic1:
    rs[i]=li.count(i)
for j in rs:
    if rs[j]==1:
        print(j)
        break;
