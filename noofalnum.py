str=input()
count=0
for i in str:
    if i.isalnum() or i==" ":
        continue
    else:
        count=count+1
print(count)

