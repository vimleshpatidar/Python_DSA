l = [10,54,98,63,47,155,1,10,5,58,5]
find = int(input("enter number to be searched :- "))
flag = False

for i in range(0,len(l)):
    if find == l[i]:
        flag = True

print(flag)