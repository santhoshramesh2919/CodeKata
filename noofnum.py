str=input()
count=0
for i in str:
    if i.isnumeric():
        count=count+1
    else:
        continue
print(count)
