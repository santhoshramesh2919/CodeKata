li=list(input())
a=0
n=0
for i in li:
    if i.isalpha():
        a=1
    elif i.isnumeric():
        n=1
if a==1 and n==1:
    print("Yes")
else:
    print("No")
