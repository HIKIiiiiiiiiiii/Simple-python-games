# Tic Tac Toe

import random as rd
import os , time
# CONST varibles
PLAYER_1 = "O"
PLAYER_2 = "X"
EMPTY = "0"
# Checking whether someone won or not
def is_win(grids = list):
    result = True
    value = 0    
    winner = str
    if grids is not None:

        if grids[0] == grids[1] == grids[2]:
            winner = grids[0]
            value = 1
        elif grids[3] == grids[4] == grids[5]:
            winner = grids[3]
            value = 1
        elif grids[6] == grids[7] == grids[8]:
            winner = grids[6]
            value = 1
        elif grids[0] == grids[3] == grids[6]:
            winner = grids[0]
            value = 1
        elif grids[1] == grids[4] == grids[7]:
            winner = grids[1]
            value = 1
        elif grids[2] == grids[5] == grids[8]:
            winner = grids[2]
            value = 1
        elif grids[0] == grids[4] == grids[8]:
            winner = grids[0]
            value = 1
        elif grids[2] == grids[4] == grids[6]:
            winner = grids[2]
            value = 1
        else:
            value = 2
        if winner != EMPTY:
            if value == 1:
                print(f"{winner} won the game!")
                result = False
            else:
                print("Draw!")
                result = False
        else:
            result = True
            
        return result
# Main running function
def TicTacToe_main():
    user_wins = 0
    user_draws = 0
    user_loses = 0
    turn = 1
    grids = [EMPTY , EMPTY , EMPTY , EMPTY , EMPTY , EMPTY , EMPTY , EMPTY , EMPTY]
    running = True

    while running:
        # Printing grids
        for i in range(9):
            if i % 3 == 0:
                print("")
            print(grids[i] , "  |   " , end = "")
        
        user_input = input(f"\nPlayer : {turn} input : ")

        if user_input.isdigit() == False :
            os.system("clear")
            print("Please input only number !") 
            continue
        elif (int(user_input) > 9) or (int(user_input)<1):
            os.system("clear")
            print("Please input only number from 1 to 9!") 
            continue
        else : 
            user_input = int(user_input) - 1           
            if grids[user_input] == EMPTY:
                if turn == 1:
                    grids[user_input] = PLAYER_1
                    turn = 2
                else:
                    grids[user_input] = PLAYER_2
                    turn = 1
            else:
                os.system("clear")
                print("Please select an empty grid!")
                continue

        running = is_win(grids)
    # End of program
    print("Thank you for playing! :)")