#prime..
n,q=map(int,input().split())
l=[]
for i in range(n+1,q):
    if i>1:
        if i==2:
            l.append(i)
        else:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                l.append(i)
for j in range(0,len(l)):
  if j==len(l)-1:
    print(l[j])
  else:
    print(l[j],end=" ")
