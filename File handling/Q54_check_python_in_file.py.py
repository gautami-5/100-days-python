## Program to check if the word "python" exists in a text file
with open ("log.txt", "r") as f:
    content = f.read()

    if ("python" in content):
        print("Yes python is present")
    else:
        print("No python is not present")