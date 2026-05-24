#take marks of 3 subjects as input and check if the student has passed or failed. The student is considered to have passed if the total marks are greater than or equal to 40% and the marks in each subject are greater than or equal to 33%.
m = input("Enter MATH marks: ")
p = input("Enter PHYSICS marks: ")
c = input("Enter CHEMISTRY marks: ")

total_per = (int(m) + int(p) + int(c))/300*100
   #assume 100 marks 
m_per = int(m)/100*100
p_per = int(p)/100*100
c_per = int(c)/100*100

if total_per >=40 and m_per >= 33 and p_per >= 33 and c_per >= 33:
    print("PASS")
else:
    print("FAIL")

