#Find topper of the class
d = {"Bheem": 95, "Chutki": 85, "Jaggu": 90,"Raju": 95}
max = 0
for x in d.values():
    if x > max:
        max = x
        print ("Max = ",max)
Top_scorers = [name for name, marks in d.items() if marks == max]
print("Top Scorers = ", Top_scorers)
