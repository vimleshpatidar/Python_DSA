l = [1,2,3,1,5,2,6,3]
seen = set()
dupli = set()

for i in l:
    if i in seen:
        dupli.add(i)
    else:
        seen.add(i)

print(dupli)

