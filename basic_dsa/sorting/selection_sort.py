l = [10,54,2,9,58,6,48,5,2,0,-1]

for j in range(0,len(l)-1):
    min_index = j
    for i in range(j+1,len(l)):
        if l[i] < l[min_index]:
            min_index = i
    flag = l[j]
    l[j] = l[min_index]
    l[min_index] = flag

print(l)