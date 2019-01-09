str=input()
count=0
for i in range(0,len(str)):
    if str[i]=="." or i==len(str)-1:
        count=count+1
    else:
        continue
print(count)
