#Even nos
l=[]
n,q=map(int,input().split())
for i in range(n+1,q):
  if i%2==1:
    l.append(i)
for j in range(0,len(l)):
  if j==len(l)-1:
    print(l[j])
  else:
    print(l[j],end=" ")
