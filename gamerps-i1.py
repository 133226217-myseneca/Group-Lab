#!/usr/bin/env python3
import random

'''
This Python program is an adaptation of the traditional game "Rock, Paper, Scissors".
The game is designed for single-player mode, where the user competes against the computer. 
The program prompts the user to input their desired choice, which could be rock, paper, or scissors.
The computer then randomly selects an option as well. 
Using the game's standard rules, the program determines the winner, and subsequently asks if the user would like to play again by prompting for a yes or no response. 
The application does not include any advanced features or graphical interface. 
The program was last updated on March 26, 2023.
'''

options = ["rock", "paper", "scissors"]

while True:
    computerOption = random.choice(options)

    print("Welcome to Rock, Paper, Scissors!")
    print("Please choose your option: rock, paper, or scissors")
    userOption = input().lower()

    if userOption not in options:
        print("Invalid option. Please try again.")
    else:
        print("You chose", userOption)
        print("The computer chose", computerOption)

        if userOption == computerOption:
            print("It's a tie!")
        elif userOption == "rock" and computerOption == "scissors":
            print("You win!")
        elif userOption == "paper" and computerOption == "rock":
            print("You win!")
        elif userOption == "scissors" and computerOption == "paper":
            print("You win!")
        else:
            print("The computer wins!")

    # If the player wants to play again or break the loop
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "no":
        break

print("Thank you for playing Rock, Paper, Scissors!")