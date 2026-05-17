d1 = {"Mumbai ": 20, "Bengaluru": 30, "Kolkata": 40, "Delhi": 50, "Hyderabad": 60}
d2 = {"Mumbai ": 25, "Bengaluru": 35, "Patna": 45, "Delhi": 55, "Goa": 65}

for x in d1:
    if x in d2:
       d1[x] = d1[x] + d2[x]
      
print(d1)
