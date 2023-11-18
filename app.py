#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import random

plays = []
wons_user = []
wons_machine = []
ties = []

def choose_machine():
    option_machine = ["rock", "paper", "scissors"]
    machine = random.choice(option_machine)
    return machine

def choose_winner(enter, machine):
    plays.append(1)
    if enter == "rock" and machine == "paper":
        print("The machine wins")
        wons_machine.append(1)
    elif enter == "rock" and machine == "scissors":
        print("You win")
        wons_user.append(1)
    elif enter == "paper" and machine == "rock":
        print("You win")
        wons_user.append(1)
    elif enter == "paper" and machine == "scissors":
        print("The machine wins")
        wons_machine.append(1)
    elif enter == "scissors" and machine == "rock":
        print("The machine wins")
        wons_machine.append(1)
    elif enter == "scissors" and machine == "paper":
        print("You win")
        wons_user.append(1)
    elif enter == machine:
        print("Tie")
        ties.append(1)
    else:
        print("Enter correctly")

def again():
    again = input("Do you want to play again? (yes/no): ")
    print("----------------------------")
    if again == "yes":
        main()
    else:
        print("Bye")

def main():
    print("Welcome to the game rock, paper or scissors")
    print("Please enter a valid option")
    for i in range(5):
        enter = input("Enter rock, paper o scissors: ")
        machine = choose_machine()
        print("Machine: ", machine)
        choose_winner(enter, machine)
        if i == 4:
            print("----------------------------")
            print("You played: ", len(plays))
            print("You won: ", len(wons_user))
            print("The machine won: ", len(wons_machine))
            print("Ties: ", len(ties))
            print("----------------------------")
            continue
    again()
main()
