word = str(input("word :- "))

flag = True
i = 0
j = len(word) - 1
while i<j: 
    if word[i] != word[j]:
        flag = False
        print(f"{word} is not palidrome")
        break
    i += 1
    j -= 1

if flag == True:
    print(f"{word} is a palindrome")

#using rev str

l = [1,2,3,1]

rev = l[::-1]

if l == rev:
    print("list is palindrome")
else:
    print("list is not palindrome")


