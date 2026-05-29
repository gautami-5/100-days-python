word = ["donkey", "ganda", "bad"]

with open("file.txt") as f:
     content = f.read()
for i in word:
    content = content.replace(i , "#")

with open ("file.txt", "w") as f:
     f.write(content)