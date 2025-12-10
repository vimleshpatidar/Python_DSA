l = [1,2,3,1,5,2,6,3]
word = "missisippi"
freq = {}

for i in l:
    freq[i] = freq.get(i,0) + 1



for ch  in word:
    freq[ch] = freq.get(ch,0) + 1

print(freq)