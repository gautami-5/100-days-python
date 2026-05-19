#Q1. Say good morning to user

name = input("Enter your name: ")
date = input("Enter date: ")
print("Good morning,",name)

#Q2. letter
#  print(f'''Dear {name},
#         You are selected!
#         {date}''') 

letter = '''Dear <NAME>,
You are selected!
<DATE>'''
print(letter.replace("<NAME>",name).replace("<DATE>",date))