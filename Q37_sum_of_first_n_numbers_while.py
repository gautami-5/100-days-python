n = int(input("Enter a number to find the sum of first n numbers: "))
i=1
total = 0
while i <= n:
    total = total + i
    i = i + 1

print(f"The sum of first {n} numbers is: {total}")
   