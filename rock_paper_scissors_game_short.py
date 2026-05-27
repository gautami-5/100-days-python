import random
computer = random.randint(-1,1)
y = input("Enter your choice:\n R = Rock\n P = Paper\n S = Scissors\n" )
c = {"R": 1, "P": -1, "S" : 0}
you = c[y.upper()]
r = {1 : "Rock", 0 : "Scissors", -1 : "Paper"}
print("You chose: ",r[you])
print("Computer chose: ",r[computer])
if computer == you:
    print("Its a tie...")
else:
    """
    if computer == -1  and you == 0:  #c - y = -1
        print("You Win!!!")
    elif computer == -1 and you == 1: #c - y = -2
        print("You lost :(")
    elif computer == 1 and you == 0: #c- y = 1
        print("You lost :(")   
    elif computer == 1 and you == -1: #c - y = 2
        print("You Win!!")
    elif computer == 0 and you == 1: #c - y = -1
        print("You Win!!")
    elif computer == 0 and you == -1: #c - y = 1
        print("You lost :(")
    
        below logic is written on basis of value of computer - you
    """
    if(computer - you == -2 or computer - you == 1 ):
        print("You lost :(")
    else:
        print("You Win!!!")
