#allow 4 friends to enter their fav language as value & key as their names. unique names

l = {}
for i in range(4):
    key = input("Enter your name: ")
    value = input(f"Enter {key} favourite language : \n")
    l[key] = value
print(l)