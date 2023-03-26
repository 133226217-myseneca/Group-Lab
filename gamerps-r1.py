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
options = ("rock", "paper", "scissors") # list of options for the computer
computer = random.choice(options) # This will choose a random option from your list for the computer


