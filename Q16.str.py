# to check if string contais double space

str = input("Enter a string: ")
x = str.find("  ")  #find method returns -1 if not found
if x == -1:
    print("String does not contain double space")
else:
    print("String contains double space at",x )  

#to check if string contains single space

y = str.find(" ")  #find method returns -1 if not found
if y == -1:
    print("String does not contain single space")
else:
    print("String contains single space at",y )