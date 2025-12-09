l = [10,54,98,63,47,155,1,0,5,58,5]
max = l[0]
for i in range(1,len(l)):
    if max < l[i]:
        max = l[i]

print(max)