# This is a classic rock paper scissors game

'''
Let's assign
rock:1
paper:2
scissors:3

According to classic rules rock-scissor-paper-rock-........ cycle is followed
'''

import random

computer = random.choice([1,2,3])

userval = input("Enter Rock, Paper or Scissors: ").capitalize()

if(userval in ["Rock","R" ,"Rck"]):
    userval="R"
elif(userval in ["Scissor","S","Sissor","Scisor","Sc"]):
    userval="S"
elif(userval in ["Paper","P","Pap","Papper","Pepper"]):
    userval="P"
else:
    print("Sorry input value not found")
    exit()

userdict = {"R": 1, "P":2 , "S":3}
reverse_user_dict = {1: "Rock" , 2:"Paper", 3:"Scissors"}
user = userdict[userval]

print(f"I choose {reverse_user_dict[computer]} and you choose {reverse_user_dict[user]}")

if(computer == user):
    print("Oh No, it's a draw")

else:
    if(computer == 1 and user==2):
        print("You won")
    elif(computer == 1 and user==3):
        print("You lost")
    elif(computer == 2 and user==1):
        print("You lost")
    elif(computer == 2 and user==3):
        print("You won")
    elif(computer == 3 and user==1):
        print("You won")
    elif(computer == 3 and user==2):
        print("You lost")
    else:
        print("An error may have occured")
