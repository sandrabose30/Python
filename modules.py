# inbuilt modules
# math
# random
# time
# os
# sys

# Math
# import math
#
# print(math.sqrt(25))
# print(math.factorial(5))
# print(math.floor(11.5))
# print(math.ceil(20.2))

# Random
import random
# print(random.randint(3,10))
#
# fruits=['apple','banana','orange',"pineapple","grapes"]
# print(random.choice(fruits))
#
# tose=["tail","head"]
# print(random.choice(tose))
#
# z=random.randint(0,1)
# print("heads") if z==1 else print("tails")

# ch=["rock","paper","scissors"]
# computer = random.choice(ch)
# player = ''
# while player not in ch:
#     player=input("enter your choice rock/paper/scissor: ").lower()
# print(f"player chose {player} and computer chose {computer}")
# if player== computer:
#     print("It's a tie")
# elif player== "rock":
#     if computer=="scissors":
#         print("Computer wins")
#     else:
#         print("Player wins")
# elif player== "paper":
#     if computer=="scissors":
#         print("Computer wins")
#     else:
#         print("Player wins")
# elif player== "rock":
#     if computer=="paper":
#         print("Computer wins")
#     else:
#         print("Player wins")

# a = "aPpLe"
# print(a.lower())
# print(a.upper())
# print(a.capitalize())

# dice game
# def dice(intial_throw):
#     count = 0
#     for i in range(intial_throw):
#         player_throw = random.randint(1,6)
#         count = count + player_throw
#     return count
#
# def dicegame():
#     intial_throw1 = random.randint(1,6)
#     print(intial_throw1, "player1 intial throw")
#     player1 = dice(intial_throw1)
#     intial_throw2 = random.randint(1,6)
#     print(intial_throw2, "player2 intial throw")
#     player2 = dice(intial_throw2)
#     if player1 > player2:
#         print("Player 1 wins!, player1 got " + str(player1) + " and player2 got " + str(player2))
#     elif player1 < player2:
#         print("Player 2 wins!, player2 got " + str(player2) + " and player1 got " + str(player1))
#     else:
#         print("It's a tie!")
#
# dicegame()



