# Rock Paper Scissor

import random as rd
import os , time

ROCK = "ROCK"
PAPER = "PAPER"
SCISSOR = "SCISSOR"

# Function to show if the user won , lost or drawn :1 = win , 0 = draw 2 = lose
def win_lose(winner = int ):
    if winner == 1 :
        print("Player won!")
    elif winner == 0:
        print("Draw!")
    else :
        print("Player lose!")

# Main runnning function
def RPS_main():
    user_wins = 0
    user_loses = 0
    user_draws = 0
    computer_choice = ""
    user_choice = ""
    choices = ["ROCK","PAPER","SCISSOR"]
    os.system("clear")
    running = True

    # Program start here
    while running:
        computer_choice = choices[rd.randint(1,3)-1]
        print("\t\tWelcome to Rock Paper Scissor game!\n")
        user_input = input("Choose one\nR: Rock\nP: Paper\nS: Scissor\nQ: Exit the program\nYour input : ").upper()
        os.system("clear")
        # Checking the input from user
        if user_input == "R" :
            user_choice = ROCK
        elif user_input == "P" :
            user_choice = PAPER
        elif user_input == "S" :
            user_choice = SCISSOR
        elif user_input == "Q" :
            running = False
            break
        else :
            
            print("Please input correctly!")
            continue

        if (user_choice == ROCK and computer_choice == SCISSOR) or (user_choice == PAPER and computer_choice == ROCK) or (user_choice == SCISSOR and computer_choice == PAPER) :
            result = 1
            user_wins += 1
        elif user_choice == computer_choice :
            result = 0
            user_draws += 1
        else :
            result = 2
            user_loses += 1
        
        print(f"You choosed : {user_choice}\nComputer choosed : {computer_choice}")
        time.sleep(2)
        print(f"Your wins : {user_wins}\nYour loses : {user_loses}\nYour draws : {user_draws}")
        win_lose(result)
        time.sleep(2)
        os.system("clear")
    # End of program
    print(f"Your wins : {user_wins}\nYour loses : {user_loses}\nYour draws : {user_draws}")
    print("Thank you for playing! :)")