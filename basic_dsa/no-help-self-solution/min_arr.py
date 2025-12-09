ar = [10,54,98,63,47,155,1,-5,58,5]
min = ar[0]
for i in range(1,len(ar)):
    if min > ar[i]:
        min = ar[i]

print(min)