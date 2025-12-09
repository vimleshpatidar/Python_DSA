l = [10,54,2,9,58,6,48,5,2,0,-1]

for i in range(0,len(l)):
    for j in range(0,len(l)-i-1):
        print(l)
        if l[j] > l[j+1]:
            flag = l[j+1]
            l[j+1] = l[j]
            l[j] = flag

print(l)



