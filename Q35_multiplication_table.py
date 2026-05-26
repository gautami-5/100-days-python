#To print multiplication table of a given number using FOR loop


x = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
     print(f"{x} x {i} = {x * i}")

#To print multiplication table of a given number using WHILE loop

i = 1
while(i<=10):
  print(f"{x} x {i} = {x * i}")
  i += 1

#To print a message for names starting with "S" in a list

l = ["Harry", "Sohan", "Sachin", "Rahul"]

for i in l:
    if(i.startswith("S")):
     print(f"{i} How are you doing?")
