l = [1,2,3,1,5,2,6,3]
seen = set()
dupli = set()

for i in l:
    if i in seen:
        dupli.add(i)
    else:
        seen.add(i)

print(dupli)

dic = {}

for j in l:
    dic[j] = dic.get(j,0) + 1

for k,v in dic.items():
    if v > 1:
        print(k, "is duplicate")

