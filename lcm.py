#LCM
n,m=map(int,input().split())
grt=max(n,m)
while 1:
    if grt%n==0 and grt%m==0:
        print(grt)
        break
    grt+=1
