x = int(input("Enter a number to check if it is prime or not: "))

if x > 1:
    for i in range(2, int(x**0.5) + 1): #x**0.5 → raise to power 0.5 (square root)
        if (x % i) == 0:
            print(f"{x} is not a prime number.")
            break
    else:
        print(f"{x} is a prime number.")