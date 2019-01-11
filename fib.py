#fibonacci
n=int(input())
n1=1
n2=1
count=0
while count < n:
       if count==n-1:
              print(n1)
       else:
              print(n1,end=' ')
              nth = n1 + n2
              n1 = n2
              n2 = nth
              count += 1
