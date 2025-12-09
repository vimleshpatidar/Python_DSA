l = [10,54,98,63,47,155,1,10,5,58,5]
find = int(input("enter number to be searched :- "))
flag = -1
index_list = []
for i in range(0,len(l)):
    if find == l[i]:
        flag = 0
        index_list.append(i)

if flag == -1:
    print("element not found")
else:
    print(f"fount the element {find} at index {index_list}")