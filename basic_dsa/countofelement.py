l = [10,54,98,10,47,155,1,-5,10,5]
target = int(input("enter number to be counted"))
count = 0
for i in l:
    if i == target:
        count += 1

print(f"your number {target} has occured {count} times.")