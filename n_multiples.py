#n multiples
n=int(input())
li=[]
for i in range(1,6):
  li.append(n*i)
for j in range(0,len(li)):
  if j==len(li)-1:
    print(li[j])
  else:
    print(li[j],end=" ")
