# Count of items of length 2 or more and 1 letter matches last letter

words  = ['abc', 'xyz', 'aba', '1221']

count = 0

for word in words:
    if len(word) > 1 and word[0] == word[-1]:
        count += 1

print (count)
