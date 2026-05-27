
def g(a,b,c):
    if a> b and a>c:
        return f"{a} is greater"
    elif b>c and b>a:
        return f"{b} is greater"
    elif c>a and c>b:
        return f"{c} is greater"
    else:
        return "all are equal"
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(g(a,b,c))