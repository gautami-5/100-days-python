x = input("Enter a sentence: ")
words = x.split()

d = {}

for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(d)