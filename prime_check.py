#prime..
n=int(input())
if n>1:
  if n==2:
    print("yes")
  else:
    for i in range(2,n):
      if n%i==0:
        print("no")
        break;
    else:
      print("yes")
      
