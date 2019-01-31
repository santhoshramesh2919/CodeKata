n,m=map(int,input().split(" "))
pro=n*m
ps=(pro)**(1/2)
if int(ps)==ps:
    print("yes")
else:
    print("no")
