x = input(print("Enter a string: "))

words = x.split()

word_frequency = {}

for y in words:
    y  = y.lower()
    if y in word_frequency:
        word_frequency[y] += 1
    else:
        word_frequency[y] = 1
        
print(word_frequency)
