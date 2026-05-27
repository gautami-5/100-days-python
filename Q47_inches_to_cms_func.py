def inches_to_cms(i):
    return i * 2.54

inches = float(input("Enter length in inches: "))
print(f"{inches} inches is equal to {inches_to_cms(inches)} cms")