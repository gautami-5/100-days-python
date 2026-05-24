names = ["Gautami", "Rahul", "Ananya", "Riya", "Arjun", "Sneha"]
n = input("Enter a name: ")

if n.capitalize() in names:
    print("Your name is present in the list.")
else:
    print("Your name is not present in the list.")