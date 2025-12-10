A = [1, 3, 5]
B = [2, 4, 6]
i,j = 0,0
merg = []
while i < len(A) and j < len(B):
    if A[i] < B[j]:
        merg.append(A[i])
        i += 1
    else:
        merg.append(B[j])
        j += 1

merg = merg + A[i:]
merg = merg + B[j:]

print(merg)
