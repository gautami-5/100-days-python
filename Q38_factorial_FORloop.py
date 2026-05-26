n = int(input("Enter a number to find factorial: "))

f = 1

for i in range(1, n+1):
    if i == 1:
        f = 1
    else:
        f = f * i

print(f"The factorial of {n} is: {f}")