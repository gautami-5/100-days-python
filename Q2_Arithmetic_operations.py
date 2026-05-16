print("Enter two integers to perform arithmetic operations")
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
sum = a + b


print("\nSum: ", sum)
difference = a - b
print("Difference: ", difference)
product = a * b
print("Product: ", product)
if b != 0:
    quotient = a / b
    print("Quotient: ", quotient)
else: 
    print("Cannot divide by zero")
division = a // b
print("Integer Division: ", division)
remainder = a % b
print("Remainder: ", remainder)