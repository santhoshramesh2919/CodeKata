#repllace * in mid
str=list(input())
if len(str)%2==1:
    str[len(str)//2]="*"
else:
    str[(len(str)//2)-1]="*"
    str[len(str)//2]="*"
print("".join(str))
