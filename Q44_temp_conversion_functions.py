def temp(c):
    f = (c * 9/5) + 32
    return f

c = int(input("Enter temperature in Celsius: "))
print(f"{c} degree Celsius is equal to {temp(c)} degree Fahrenheit")