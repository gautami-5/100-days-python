m = int(input("Enter total marks: "))

if m >= 90 and m <= 100:
    print("Grade Excellent")
elif m >= 80 and m < 90:
    print("Grade A")
elif m >= 70 and m < 80:
    print("Grade B")
elif m >= 60 and m < 70:
    print("Grade C")
elif m >= 50 and m < 60:
    print("Grade D")
elif m <50:
    print("Grade F")
else:
    print("Invalid marks")

