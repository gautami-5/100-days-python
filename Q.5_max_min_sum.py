#Find the maximum, minimum and sum of the given tuple without using built-in functions.
#t = ("Mumbai","Bengaluru","Kolkata","Delhi","Hyderabad")
#print(t[0],t[4],t[2])

t2 = (63,54,19,64,17)
max = t2[0]
min = t2[0]
#For max
for x in t2:
    if x > max:
        max = x
        print ("Max = ",max)
#For min
for x in t2:
    if x < min:
        min = x
print("Min = ",min)
#For sum
sum = 0
for x in t2:
    sum = sum + x
    
print("Sum = ",sum)
        
