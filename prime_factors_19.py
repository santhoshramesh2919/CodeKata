def isprime(n):
  if n==2:
    return True
  else:
    for j in range(2,n):
      if n%j==0:
        return False
    else:
      return True

n=int(input())
li=[]
for i in range(2,n+1):
  if n%i==0 and isprime(i):
    li.append(i)
print(*li)
