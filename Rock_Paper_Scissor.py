"""
Workflow of project
1- Input from user(Rock , Paper , Scissor)one of them
2-Computer choice (computer will choose randomly by importing Random module)
3-Result

Cases
A- Rock
Rock-Rock = tie
Rock-paper = Paper wins the game
Rock-scissor = Rock wins the game

B- Paper
Paper-Paper = tie
Paper-Rock = Paper wins the game
Paper-Scissor = Scissor wins the game

C- Scissor
Scissor-Scissor = tie
Scissor-paper = Scissor
Scissor - Rock = Rock


    """

import random
item_list = ["Rock" , "Paper" ,"Scissor"]

User_choice = input("Enter you move: Rock , Paper , Scissor  ")
computer_choice = random.choice(item_list)
print(f"User choice = {User_choice} , computer choice = {computer_choice}")


if User_choice == computer_choice:
    print("Both chooses same : Match Tie")
elif User_choice == "Rock":
    if computer_choice == "Paper":
        print("Paper covers Rock : Computer Won")
    else:
        print("Rock smashes Scissor : You Won")
elif User_choice == "Paper":
    if computer_choice == "Rock":
        print("Paper covers Rock : You Won")
    else:
        print("Scissor cuts Paper : Computer Won")
elif User_choice == "Scissor":
    if computer_choice == "Rock":
        print("Rock smashes scissor : Computer won")
    else:
        print("Scissor cuts paper : You Won")