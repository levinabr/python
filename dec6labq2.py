"""
Author : Levin Abraham Jacob
Write a program to play a sticks game in which there are 16 sticks.
Two players take turns to play the game. Each player picks one set of sticks (needn’t be adjacent) during his turn.
A set contains 1, 2, or 3 sticks. The player who takes the last stick is the loser.
The number of sticks in the set is to be input."""

print("Welcome to the Game of sticks!!!!")
player_1 = input("Enter the name of player 1:")
player_2 = input("Enter the name of player 2:")
stick = 16
while stick !=0:
    if stick !=0 :
        print (stick)
        choice = int(input(f"{player_1} Enter a Number from (1,2,3)"))
        stick=stick-choice
        player = player_1
    if stick !=0 :
        print(stick)
        choice =int(input(f"{player_2} Enter a Number from (1,2,3)"))
        stick=stick-choice
        player = player_2

    if stick==0 :
       print(f"{player} has lost the game")