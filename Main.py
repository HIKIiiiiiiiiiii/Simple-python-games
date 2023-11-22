import libra
import random , time , os
# Number of games
GAMES = 2
# Ye sure it is bad naming :/
def main_main():
    print("#Made by hiki a.k.a iFrit\n")
    print("\t\tWelcome!\n")
    print("1. Rock Paper Scissor")
    print("2. Tic Tac Toe")
    print("Input which game you want to play")
    print("Or enter \"Q\" to quit the program")

    while True:
        # User choice
        user_input = input("User input : ").upper()

        if user_input == "Q":
            print("Goodbye :)")
            break
        if user_input.isdigit() == False:
            print("Please only input number")
            continue
        else:
            # User input is a legit degit number hence we turn it to int
            user_input = int(user_input)

            if user_input > GAMES:
                print("Please select one of the game or enter \"Q\" to quit!")
                continue
            # Clearing screen before running the program
            os.system("clear")

            if user_input == 1:
                libra.RPS.RPS_main()
            elif user_input == 2:
                libra.TicTacToe.TicTacToe_main()