import random
def game():
    print("You are playing the GAME.")
    score = random.randint(1,50)
    print("Your score: ",score)
    f = open("hi_score.txt")
    hi_score = f.read()
    if (hi_score != ""):
        hi_score = int(hi_score)
    else:
        hi_score = 0
    f.close()
    if(score>hi_score):
        f = open("hi_score.txt","w")
        f.write(str(score))
        f.close()
    return score
    
    

game()