'''
n = 3

***
**
*

'''

def star_pattern(n):
   if n == 1:
        print("*")
   else:
        print('*'*n)
        star_pattern(n-1)

n = int(input("Enter a number: "))
star_pattern(n)