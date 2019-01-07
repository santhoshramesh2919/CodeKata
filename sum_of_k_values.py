#sum of k integers 
n,k=map(int,input().split())
integers=list((map(int,input().split(" "))))
sum1=0
for i in range(0,k):
  sum1=sum1+integers[i]
print(sum1)
