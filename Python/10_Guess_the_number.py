import random
target=random.randint(1,50)
i=0
while True:
    user_choice=int(input("enter a number:"))
    if (i>=5):
        print("you have lost the Game.")
        break
    if(user_choice==target):
        print("Success!")
        break
    elif(user_choice<target):
        print("Your choice is too small,Guess a big one: ")
    else:
        print("Your choice is too big , Guess a small one: ")
    i+=1

print("----Game_Over----")
