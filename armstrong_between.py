#ARmstrong between
n,q=map(int,input().split())
l=[]
for i in range(n+1,q):
    t=i
    r,s=0,0
    while i>0:
        r=i%10
        s=s+r**3 
        i=i//10
    if t==s:
        l.append(t)
for j in range(0,len(l)):
  if j==len(l)-1:
    print(l[j])
  else:
    print(l[j],end=" ")
