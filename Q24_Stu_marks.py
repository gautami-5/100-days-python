students = {
    "Gautami": 92,
    "Rahul": 75,
    "Ananya": 88,
    "Riya": 95,
    "Arjun": 67
}
l = []
for x in students:
    if students[x] > 75:
        l.append(x)
print("Students with marks greater than 75: ", l)  
highest_marks = 0
s = ''
for x in students:
    if students[x] > highest_marks:
        highest_marks = students[x]
        s = x
print("\nStudent with highest marks: ", s,highest_marks) 