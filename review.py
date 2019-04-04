import random

print("Hello Welcome to rock paper scissors!")
print("Please select Rock(r), Paper(p) or Scissors(s)")


valid = False
choice = input("> ")
while valid == False:
    if choice.lower() == "r" or choice.lower() == "s" or choice.lower() == "p":
        valid = True
    else:
        choice = input("Please put in a valid value =>")

user_choice = {"r" : "Rock", "p" : "Paper", "s" : "Scissors"}
choices = {0 : "Rock", 1 : "Paper", 2 : "Scissors"}
comp_choice = choices[random.randint(0,2)]
user_pick = user_choice[choice]

print("You played: ", user_pick)
print("The Computer played: ", comp_choice)


if user_pick == comp_choice:
    print("Draw!!!")
elif user_pick == "Rock" and comp_choice == "Scissors":
    print("You win!!!")
elif user_pick == "Paper" and comp_choice == "Rock":
    print("You win!!!")
elif user_pick == "Rock" and comp_choice == "Paper":
    print("You lose...")
elif user_pick == "Paper" and comp_choice == "Scissors":
    print("You lose...")
