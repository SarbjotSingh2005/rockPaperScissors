#Project for codsoft internship 
#Project name :- rock, paper or scissors 
import random
print(" rules for the game is mentioned below:-")
print("rock vs paper = paper wwins\n paper vs scissors = scissors wins\n scissors vs rock = rock wins")
print("choose your side:- \n 1:- Rock \n 2:- Paper \n 3:- Scissors")
user_choice = int(input("enter the number which you selected :-"))
choices = [1,2,3]
#in choices 1,2,3 is as same as for user
computer_choice = random.choice(choices)
if user_choice==1:
    print("you selected :- Rock ")
elif user_choice==2:
    print("you selected :- Paper")
elif user_choice==3:
    print("you selected :- Scissors")
else:
    print("invalid input")
print("computer selected:-",computer_choice)
if user_choice==computer_choice:
    print("it's a tie ")
elif user_choice==1:
    if computer_choice == 2:
        print("paper smashes rock & computer wins")
    else:
        print("rock smashes scissors &  you win")
elif user_choice==2:
    if computer_choice==1:
        print("paper smashes rock & you win")
    else:
        print("scissors smashes paper & computer wins")
elif user_choice==3:
    if computer_choice==1:
        print("rock smashes scissors & computer wins")
    else:
        print("scissors smashes paper &  you win")
else:
    print("invalid input by user")