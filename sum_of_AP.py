#arithmetic progression
n,a,d=map(int,input().split(" "))
sum =a
for i in range(1,n):
  a=a+d
  sum=sum+a
print(sum)
