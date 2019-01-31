str=list(input())
num=""
for i in str:
    if i.isnumeric():
        num=num+i
print(num)
