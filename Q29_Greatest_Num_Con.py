#find greatest number among 4 numbers entered by user
a = int(input("Enter integer: "))
b = int(input("Enter integer: "))
c = int(input("Enter integer: "))
d = int(input("Enter integer: "))
    
if a > b and a > c and a > d:
    {print(f"{a} is greatest")}
elif b > a and b > c and b > d:
    {print(f"{b} is greatest")}
elif c > a and c > b and c > d:
    {print(f"{c} is greatest")}
else:
    {print(f"{d} is greatest")}