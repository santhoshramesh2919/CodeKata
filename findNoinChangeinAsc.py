n=int(input())
li=list(map(int,input().split()))
lis=sorted(li)
for i in range(0,len(li)):
    if li[i]==lis[i]:
        continue
    else:
        print(i)
        break
