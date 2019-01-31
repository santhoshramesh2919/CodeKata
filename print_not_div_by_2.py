#print_no_not divisible by 2
n=int(input())
while (n!=0):
    if n%2==0:
        n=n//2
    else:
        print(n)
        break
