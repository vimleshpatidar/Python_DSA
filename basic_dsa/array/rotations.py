l = [1,2,3,1,5,2,6,3]

#right rotations
k = 1
k = k % len(l) # if rotation value is more than lenght of arr
right_rotated = l[-k:] + l[:-k]
print(right_rotated)

#left rotation 

left = l[k:] + l[0:k] 

print(left)