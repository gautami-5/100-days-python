n = int(input("Enter number to print multiplication table in reverse:"))

for i in range(10, 0, -1):
    print(f"{n} x {i} = {n*(i)}")